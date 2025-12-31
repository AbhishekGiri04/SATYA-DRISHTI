from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="SATYA-DRISHTI - Minimal Version", 
    version="2.0.0",
    description="Developed by Abhishek Giri"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    url: str
    deep_analysis: bool = False

@app.get("/")
def root():
    return {
        "message": "SATYA-DRISHTI API is running (Minimal Version)",
        "developer": "Abhishek Giri",
        "github": "https://github.com/abhishekgiri04"
    }

@app.post("/analyze/")
async def analyze_content(request: AnalyzeRequest):
    return {
        "analysis_id": "demo-123",
        "url": request.url,
        "status": "success",
        "risk_assessment": {
            "score": 25,
            "level": "LOW",
            "factors": ["demo_mode"]
        },
        "content_analysis": {
            "sentiment": {"label": "NEUTRAL", "score": 0.5},
            "toxicity": {"is_toxic": False, "confidence": 0.1},
            "message": "Demo mode - Install AI dependencies for full analysis"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "mode": "minimal"}