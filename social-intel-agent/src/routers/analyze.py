from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.universal_dispatcher import UniversalAnalysisDispatcher
from src.database.mongodb import mongodb
import asyncio
from datetime import datetime
import uuid

router = APIRouter(prefix="/analyze", tags=["analysis"])

class AnalyzeRequest(BaseModel):
    url: str
    deep_analysis: bool = False

@router.post("/")
async def analyze_content(request: AnalyzeRequest):
    try:
        # Try real AI analysis with 60 second timeout
        dispatcher = UniversalAnalysisDispatcher()
        result = await asyncio.wait_for(
            dispatcher.analyze(request.url, request.deep_analysis),
            timeout=60.0
        )
        
        # Save to MongoDB if connected (don't wait for response)
        if mongodb.client:
            try:
                await mongodb.save_analysis(result.copy())
            except Exception as e:
                print(f"Failed to save to MongoDB: {e}")
        
        return result
    except asyncio.TimeoutError:
        print("⚠️ AI Analysis timeout - returning demo response")
        return generate_demo_response(request.url)
    except ImportError as e:
        print(f"⚠️ AI models not available: {e} - returning demo response")
        return generate_demo_response(request.url)
    except Exception as e:
        print(f"⚠️ Analysis failed: {e} - returning demo response")
        return generate_demo_response(request.url)

def generate_demo_response(url: str):
    """Generate demo response when AI models fail or timeout"""
    return {
        "analysis_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "url": url,
        "platform": "unknown",
        "status": "completed",
        "metadata": {
            "title": "Content Analysis (Demo Mode)",
            "author": "Demo",
            "published_at": datetime.utcnow().isoformat()
        },
        "risk_assessment": {
            "score": 25,
            "level": "LOW",
            "confidence": 0.75,
            "factors": ["demo_mode"],
            "reasons": ["⚠️ Running in demo mode - AI models unavailable or timed out"]
        },
        "content_analysis": {
            "sentiment": {"label": "NEUTRAL", "score": 0.5, "confidence": 0.7},
            "toxicity": {"is_toxic": False, "confidence": 0.2},
            "hate_speech": {"is_hate_speech": False, "confidence": 0.1, "label": "not_hate"},
            "content_categories": {
                "primary_category": "general",
                "detected_categories": ["demo"],
                "is_flagged": False
            },
            "intent": {"intent": "informational", "confidence": 0.5},
            "nsfw": {"is_nsfw": False, "confidence": 0.1}
        },
        "image_analysis": [],
        "combined_risk": {
            "score": 25,
            "level": "LOW",
            "text_risk": 25,
            "image_risk": 0
        },
        "language_analysis": {
            "detected_language": "en",
            "language_name": "English",
            "is_indian_language": False,
            "bhashini_enabled": False
        },
        "source_verification": {
            "vishwaas_score": 50,
            "verification_status": "UNVERIFIED",
            "source_category": "unknown",
            "credibility_multiplier": 1.0
        },
        "summary": "⚠️ Demo Mode: AI models are unavailable or took too long to respond. This is sample data for testing. For real analysis, ensure all AI dependencies are properly installed.",
        "text_preview": "Content preview not available in demo mode. Please check AI model installation."
    }