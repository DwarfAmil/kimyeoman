import bcrypt
from app.DB.database import userDB
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: str
    password: str


def create_hash(target: str):
    return bcrypt.hashpw(target.encode("utf-8"), bcrypt.gensalt())


@router.post("/sign-up")
async def sign_up(user: User):
    userDB.execute("INSERT INTO user_data VALUES(?, ?, ?)", (user.id, create_hash(user.password), create_hash(user.id + user.password)))
    userDB.commit()

    return {"message": "Sign up success"}


@router.post("/sign-in")
async def sign_in(user: User):
    cursor = userDB.execute("SELECT * FROM user_data WHERE id=?", (user.id,)).fetchone()

    is_password_same = bcrypt.checkpw(user.password.encode("utf-8"), cursor[1])

    if is_password_same:
        return cursor[2]


@router.post("/unregister")
async def unregister(user: User):
    cursor = userDB.execute("SELECT * FROM user_data WHERE id=?", (user.id,)).fetchone()

    is_password_same = bcrypt.checkpw(user.password.encode("utf-8"), cursor[1])

    if is_password_same:
        userDB.execute("DELETE FROM user_data WHERE id=?", (user.id,))
        userDB.commit()

        return {"message": "Unregister success"}
    else:
        return {"message": "Unregister failed"}
