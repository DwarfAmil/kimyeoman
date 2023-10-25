import deepl
from fastapi import APIRouter

router = APIRouter()

auth_key = "API_KEY"
translator = deepl.Translator(auth_key)


@router.post("/translate_ko_to_en")
async def translate(text: str):
    return translator.translate_text(text, target_lang="EN-US")


@router.post("/translate_en_to_ko")
async def translate(text: str):
    return translator.translate_text(text, target_lang="KO")
