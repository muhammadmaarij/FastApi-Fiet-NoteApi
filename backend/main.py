from fastapi import FastAPI
from backend.routes import note, user

app = FastAPI()

app.include_router(note.router, prefix="/notes", tags=["notes"])
app.include_router(user.router, prefix="/users", tags=["users"])

# Run the server with:
# uvicorn backend.main:app --reload
