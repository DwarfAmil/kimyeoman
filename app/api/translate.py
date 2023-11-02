import os

from dotenv import load_dotenv
import deepl
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

load_dotenv()

auth_key = os.environ.get("DEEPL_API_KEY")
translator = deepl.Translator(auth_key)


class Text(BaseModel):
    lang: str
    text: str


@router.post("/translate")
async def translate(text: Text):
    return translator.translate_text(text.text, target_lang=text.lang)
