from fastapi import APIRouter
from pydantic import BaseModel

from app.DB.database import chatDB

router = APIRouter()


class Chat(BaseModel):
    char: int
    chat: str


class Char(BaseModel):
    char: int


@router.post("/upload")
async def upload(chat: Chat):
    if chatDB.execute("SELECT * FROM chat_data WHERE id=?", (chat.char,)).fetchone() is not None:
        chatDB.execute("UPDATE chat_data SET chat=? WHERE id=?", (chat.chat, chat.char))
    else:
        chatDB.execute("INSERT INTO chat_data VALUES(?, ?)", (chat.char, chat.chat))
    chatDB.commit()

    return {"message": "Upload success"}


@router.post("/download")
async def download(char: Char):
    return {"chat": chatDB.execute("SELECT * FROM chat_data WHERE id=?", (char.char,)).fetchone()[1]}
