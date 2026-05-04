from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.dependencies.auth import get_current_user
from backend.app.schemas.notes import NoteCreate, NoteUpdate
from backend.app.services.firestore_service import save_note, load_notes, update_note_in_db, delete_note_in_db
from backend.app.services.ollama_service import summarize_notes

router = APIRouter(prefix="/notes", tags=["notes"])
@router.post("")
def create_note(payload: NoteCreate, user=Depends(get_current_user)):
    try:
        note = save_note(user["uid"], payload.title, payload.content)
        return note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("")
def get_notes(limit: int = Query(default=20, ge=1, le=100), user=Depends(get_current_user)):
    try:
        notes = load_notes(user["uid"], limit=limit)
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{note_id}")
def update_note(note_id: str, payload: NoteUpdate, user=Depends(get_current_user)):
    try:
        updated_note = update_note_in_db(user["uid"], note_id, payload.title, payload.content)
        return updated_note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{note_id}")
def delete_note(note_id: str, user=Depends(get_current_user)):
    try:
        delete_note_in_db(user["uid"], note_id)
        return {"message": "Ghi chú đã được xóa"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/summarize")
def summarize_all_notes(user=Depends(get_current_user)):
    try:
        notes = load_notes(user["uid"], limit=100)
        if not notes:
            return {"summary": "Bạn chưa có ghi chú nào để tóm tắt."}
        
        summary = summarize_notes(notes)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/summarize/{note_id}")
def summarize_single_note(note_id: str, user=Depends(get_current_user)):
    try:
        notes = load_notes(user["uid"], limit=100)
        note = next((n for n in notes if n["id"] == note_id), None)
        if not note:
            raise HTTPException(status_code=404, detail="Ghi chú không tồn tại")
        
        summary = summarize_notes([note])
        return {"summary": summary}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    