from fastapi import FastAPI
from pydantic import BaseModel 
from openai import OpenAI


app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health_get():
    return {"status": "Ok"}

llm = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="anything")
@app.post("/api/chat")
def chat(req: ChatRequest) -> dict:
    try:
        resp = llm.chat.completions.create(model="ovh/Meta-Llama-3_3-70B-Instruct", messages=[{"role": "user", "content": req.message}])
        return {"reply": resp.choices[0].message.content, "provider": getattr(getattr(resp, "x_freellmpool", None), "provider", "unknown"), "model": resp.model}
    except Exception as exc:
        return {"error" : str(exc)}