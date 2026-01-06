from fastapi import FastAPI
from pydantic import BaseModel
from backend.core.distillation import distill_story


app = FastAPI(title="Producer Lens")


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {"status": "Producer Lens backend running"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    distilled = distill_story(request.text)

    return {
        "product": "Producer Lens",
        "stage": "story_distillation",
        "output": distilled
    }

