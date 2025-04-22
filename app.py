from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Initialize the model
translator = pipeline("text2text-generation", model="codellama/CodeLlama-7b-Instruct-hf")

class CodeRequest(BaseModel):
    code: str
    target_lang: str

@app.post("/translate")
def translate_code(data: CodeRequest):
    prompt = f"Translate this code to {data.target_lang}:\n\n{data.code}"
    output = translator(prompt, max_new_tokens=512)[0]['generated_text']
    return {"translated_code": output}

