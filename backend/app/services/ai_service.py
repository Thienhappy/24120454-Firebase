from dotenv import load_dotenv
load_dotenv()

import os
from google import genai

# Tự động lấy API key từ file môi trường (.env)
def summarize_notes(notes: list[dict]) -> str:
    """Tóm tắt nội dung danh sách ghi chú bằng AI sử dụng thư viện google-genai mới"""
    
    # 1. Kiểm tra API Key (có thể thay đổi cách lấy tùy thuộc vào kiến trúc của bạn)
    api_key = os.getenv("GEMINI_API_KEY") 
    if not api_key:
        return "Lỗi: Chưa cấu hình GEMINI_API_KEY. Vui lòng thêm vào file .env"
    
    # 2. Khởi tạo Client bằng thư viện mới
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
         return f"Lỗi khởi tạo Client: {e}"

    # 3. Chuẩn bị dữ liệu đầu vào
    if not notes:
        return "Không có ghi chú nào để tóm tắt."

    text_to_summarize = "Danh sách ghi chú của tôi:\n\n"
    for idx, note in enumerate(notes, 1):
        title = note.get("title", "Không tiêu đề")
        content = note.get("content", "")
        text_to_summarize += f"Ghi chú {idx} - {title}:\n{content}\n\n"
    
    text_to_summarize += "\nHãy tổng hợp lại các ghi chú này một cách ngắn gọn, súc tích và dễ hiểu nhất cho tôi."

    # 4. Gọi Model để sinh nội dung
    try:
        # Sử dụng model flash mới nhất. Bạn có thể đổi sang 'gemini-2.0-flash' nếu hệ thống đã hỗ trợ.
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=text_to_summarize,
        )
        return response.text
    except Exception as e:
        return f"Lỗi AI: {e}"