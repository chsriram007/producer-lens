from fastapi import FastAPI
from pydantic import BaseModel
from backend.core.distillation import distill_story
from backend.services.ai_engine import AIEngine
ai_engine = AIEngine()


app = FastAPI(title="Producer Lens")


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {"status": "Producer Lens backend running"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    distilled = distill_story(request.text)
    enhanced = ai_engine.enhance_story(distilled)

    return {
        "product": "Producer Lens",
        "stage": "story_distillation",
        "output": enhanced
    }


