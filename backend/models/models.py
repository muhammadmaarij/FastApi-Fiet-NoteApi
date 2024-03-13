from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # notes = relationship("Note", back_populates="owner")


# class Note(Base):
#     __tablename__ = 'notes'

#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(Text)
#     owner_id = Column(Integer, ForeignKey('users.id'))
#     owner = relationship("User", back_populates="notes")

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
