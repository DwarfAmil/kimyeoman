import deepl
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

auth_key = ""
translator = deepl.Translator(auth_key)


class Text(BaseModel):
    lang: str
    text: str


@router.post("/translate")
async def translate(text: Text):
    return translator.translate_text(text.text, target_lang=text.lang)
