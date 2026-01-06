from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Producer Lens")


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {"status": "Producer Lens backend running"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    return {
        "product": "Producer Lens",
        "status": "received",
        "next": "analysis pending",
        "input_preview": request.text[:100]
    }
