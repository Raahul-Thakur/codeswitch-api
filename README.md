# CodeSwitch API (FastAPI + Transformers)

This backend API receives code + target language and returns the translated version using a Hugging Face model.

### Endpoint:
`POST /translate`

Payload:
```json
{
  "code": "def add(a, b): return a + b",
  "target_lang": "Java"
}

```
Response:
```json
{
  "translated_code": "public int add(int a, int b) { return a + b; }"
}
```
