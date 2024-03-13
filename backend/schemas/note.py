# from pydantic import BaseModel


# class NoteBase(BaseModel):
#     content: str


# class NoteCreate(NoteBase):
#     pass


# class NoteDisplay(NoteBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


from pydantic import BaseModel


class NoteBase(BaseModel):
    content: str


class NoteCreate(NoteBase):
    pass


class NoteDisplay(NoteBase):
    id: int

    class Config:
        orm_mode = True
