import os
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])

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
