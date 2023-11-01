import os
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.translate import router as translator_router
from app.api.chat import router as chat_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(translator_router, prefix="/translator", tags=["translate"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(request: Request):
    return {"message": "Hello World"}


if __name__ == "__main__":
    os.system("python -m uvicorn main:app")
