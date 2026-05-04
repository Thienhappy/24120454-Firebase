import streamlit as st
import requests

from api_client import (
    signup, login, google_login, 
    create_note, get_notes, update_note, delete_note, 
    summarize_all_notes, summarize_single_note
)

st.set_page_config(page_title="Simple Notes", page_icon="📝")

if "user" not in st.session_state:
    st.session_state.user = None

if "notes" not in st.session_state:
    st.session_state.notes = []

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if "show_login" not in st.session_state:
    st.session_state.show_login = True


def load_history():
    if not st.session_state.user:
        return
    try:
        # Load lịch sử ghi chú thay cho chat
        notes = get_notes(st.session_state.user["idToken"])
        st.session_state.notes = notes
    except Exception:
        st.session_state.notes = []


def clear_google_query_params():
    try:
        st.query_params.clear()
    except Exception:
        pass


def handle_google_login_callback():
    if st.session_state.user:
        return

    params = st.query_params
    raw_token = params.get("id_token")

    if not raw_token:
        return

    id_token = raw_token[0] if isinstance(raw_token, list) else raw_token

    try:
        user = google_login(id_token)
        st.session_state.user = user
        load_history()
        clear_google_query_params()
        st.success("Đăng nhập Google thành công")
        st.rerun()
    except requests.HTTPError as e:
        st.error(f"Đăng nhập Google thất bại: {e}")
        clear_google_query_params()
    except Exception as e:
        st.error(f"Lỗi xử lý Google login: {e}")
        clear_google_query_params()


def login_form():
    st.subheader("Đăng nhập")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Đăng nhập")
        goto_signup = st.form_submit_button("Chưa có tài khoản? Đăng ký")

    if goto_signup:
        st.session_state.show_signup = True
        st.session_state.show_login = False
        st.rerun()

    if submitted:
        try:
            user = login(email, password)
            st.session_state.user = user
            load_history()
            st.success("Đăng nhập thành công")
            st.rerun()
        except requests.HTTPError as e:
            st.error(f"Đăng nhập thất bại: {e}")
        except Exception as e:
            st.error(f"Lỗi đăng nhập: {e}")

    st.markdown("### Hoặc")

    google_login_url = dict(st.secrets["google-login"])["google-url"]

    if google_login_url:
        st.markdown(
        f'''
        <a href="{google_login_url}" target="_self" style="
            display: inline-block;
            width: 100%;
            text-align: center;
            padding: 0.6rem 1rem;
            background-color: white;
            color: black;
            text-decoration: none;
            border-radius: 0.5rem;
            border: 1px solid #ddd;
            font-weight: 600;
        ">
            Đăng nhập với Google
        </a>
        ''',
        unsafe_allow_html=True,
    )
    else:
        st.info(
            "Chưa cấu hình Google-login trong secrets. "
            "Hãy thêm URL đăng nhập Google để dùng tính năng này."
        )


def signup_form():
    st.subheader("Đăng ký")
    with st.form("signup_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Tạo tài khoản")
        goto_login = st.form_submit_button("Đã có tài khoản? Đăng nhập")

    if goto_login:
        st.session_state.show_signup = False
        st.session_state.show_login = True
        st.rerun()

    if submitted:
        try:
            signup(email, password)
            st.success("Tạo tài khoản thành công, hãy đăng nhập")
            st.session_state.show_signup = False
            st.session_state.show_login = True
            st.rerun()
        except requests.HTTPError as e:
            st.error(f"Đăng ký thất bại: {e}")
        except Exception as e:
            st.error(f"Lỗi đăng ký: {e}")


handle_google_login_callback()

st.title("Simple Notes 📝")

if st.session_state.user:
    st.success(f"Đang đăng nhập: {st.session_state.user['email']}")
    if st.button("Đăng xuất"):
        st.session_state.user = None
        st.session_state.notes = []
        clear_google_query_params()
        st.rerun()
else:
    if st.session_state.show_signup:
        signup_form()
    else:
        login_form()

st.divider()

if st.session_state.user:
    st.subheader("🤖 AI Tóm tắt")
    if st.button("Tóm tắt tất cả ghi chú"):
        with st.spinner("Đang nhờ AI tóm tắt..."):
            try:
                res = summarize_all_notes(st.session_state.user["idToken"])
                st.info(res.get("summary", "Không có dữ liệu"))
            except Exception as e:
                st.error(f"Lỗi AI: {e}")
                
    st.divider()
    st.subheader("📚 Danh sách Ghi chú")
    
    if not st.session_state.notes:
        st.write("Bạn chưa có ghi chú nào.")
        
    for note in list(st.session_state.notes):
        with st.expander(note["title"]):
            st.write(note["content"])
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Xóa", key=f"del_{note['id']}"):
                    delete_note(st.session_state.user["idToken"], note["id"])
                    load_history()
                    st.rerun()
            with col2:
                if st.button("Tóm tắt", key=f"sum_{note['id']}"):
                    with st.spinner("AI đang tóm tắt ghi chú này..."):
                        try:
                            res = summarize_single_note(st.session_state.user["idToken"], note["id"])
                            st.info(res.get("summary", ""))
                        except Exception as e:
                            st.error(f"Lỗi: {e}")

    st.divider()
    st.subheader("✍️ Tạo ghi chú mới")
    note_name = st.text_input("Tiêu đề")
    note_content = st.text_area("Nội dung...", height=200)
    if note_name and note_content:
        if st.button("Tạo ghi chú"):
            try:
                create_note(st.session_state.user["idToken"], note_name, note_content)
                st.success("Tạo thành công!")
                load_history()  # Load lại list sau khi tạo
                st.rerun()
            except Exception as e:
                st.error(f"Lỗi khi tạo ghi chú: {e}")