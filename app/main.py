import os
from fastapi import FastAPI, Request

from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
def read_root(request: Request):
    return {"message": "Hello World"}


if __name__ == "__main__":
    os.system("python -m uvicorn main:app")
