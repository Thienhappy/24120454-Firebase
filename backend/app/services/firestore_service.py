from datetime import datetime, timezone
from backend.app.core.firebase_config import get_firestore
from firebase_admin import firestore

db = get_firestore()

def save_note(uid: str, title: str, content: str):
    doc = {
        "title": title,
        "content": content,
        "ts": datetime.now(timezone.utc)
    }
    _, doc_ref = db.collection("notes").document(uid).collection("user_notes").add(doc)
    doc["id"] = doc_ref.id
    return doc

def load_notes(uid: str, limit: int = 20):
    q = (
        db.collection("notes")
        .document(uid)
        .collection("user_notes")
        .order_by("ts", direction=firestore.Query.DESCENDING)
        .limit(limit)
    )

    docs = list(q.stream())
    docs.reverse()

    return [
        {
            "id": d.id,
            "title": d.to_dict().get("title", ""),
            "content": d.to_dict().get("content", "")
        }
        for d in docs
    ]

def update_note_in_db(uid: str, note_id: str, title: str, content: str):
    doc_ref = db.collection("notes").document(uid).collection("user_notes").document(note_id)
    doc_ref.update({
        "title": title,
        "content": content,
        "ts": datetime.now(timezone.utc)
    })
    return {"id": note_id, "title": title, "content": content}

def delete_note_in_db(uid: str, note_id: str):
    db.collection("notes").document(uid).collection("user_notes").document(note_id).delete()


