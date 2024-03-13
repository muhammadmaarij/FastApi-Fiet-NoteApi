# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List
# from backend.schemas.note import NoteCreate, NoteDisplay
# from backend.models.models import Note
# from backend.db.database import get_db

# router = APIRouter()


# @router.get("/", response_model=List[NoteDisplay])
# def get_notes(db: Session = Depends(get_db)):
#     return db.query(Note).all()


# @router.get("/{note_id}", response_model=NoteDisplay)
# def get_note(note_id: int, db: Session = Depends(get_db)):
#     note = db.query(Note).filter(Note.id == note_id).first()
#     if note is None:
#         raise HTTPException(status_code=404, detail="Note not found")
#     return note


# @router.post("/", response_model=NoteDisplay)
# def create_note(note: NoteCreate, db: Session = Depends(get_db)):
#     new_note = Note(content=note.content)
#     db.add(new_note)
#     db.commit()
#     db.refresh(new_note)
#     return new_note


# @router.put("/{note_id}", response_model=NoteDisplay)
# def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db)):
#     db_note = db.query(Note).filter(Note.id == note_id).first()
#     if db_note is None:
#         raise HTTPException(status_code=404, detail="Note not found")
#     db_note.content = note.content
#     db.commit()
#     db.refresh(db_note)
#     return db_note


# @router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_note(note_id: int, db: Session = Depends(get_db)):
#     db_note = db.query(Note).filter(Note.id == note_id).first()
#     if db_note is None:
#         raise HTTPException(status_code=404, detail="Note not found")
#     db.delete(db_note)
#     db.commit()
#     return {"ok": True}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.models.models import Note
from backend.schemas.note import NoteCreate, NoteDisplay
from backend.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[NoteDisplay])
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()


@router.post("/", response_model=NoteDisplay)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
