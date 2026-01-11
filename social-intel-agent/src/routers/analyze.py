from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.universal_dispatcher import UniversalAnalysisDispatcher

router = APIRouter(prefix="/analyze", tags=["analysis"])

class AnalyzeRequest(BaseModel):
    url: str
    deep_analysis: bool = False

@router.post("/")
async def analyze_content(request: AnalyzeRequest):
    try:
        dispatcher = UniversalAnalysisDispatcher()
        result = await dispatcher.analyze(request.url, request.deep_analysis)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))