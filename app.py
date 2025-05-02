from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
translator = pipeline("text2text-generation", model="Salesforce/codet5-small")

class CodeRequest(BaseModel):
    code: str
    target_lang: str

@app.post("/translate")
def translate_code(data: CodeRequest):
    prompt = f"Translate this code to {data.target_lang}:\n\n{data.code}"
    output = translator(prompt, max_new_tokens=256)[0]['generated_text']
    return {"translated_code": output}
