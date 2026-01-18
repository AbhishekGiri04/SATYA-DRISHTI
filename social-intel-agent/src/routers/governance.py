from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.config.logger import setup_logger
from datetime import datetime, timedelta
from src.database.mongodb import mongodb

logger = setup_logger(__name__)
router = APIRouter()

class AnalysisQuery(BaseModel):
    analysis_id: str

@router.get("/governance/stats/dashboard")
async def get_dashboard_stats():
    """Get governance dashboard statistics"""
    try:
        if not mongodb.client:
            return {
                "daily_analysis": {
                    "total_content_analyzed": 0,
                    "high_risk_detected": 0,
                    "reports_generated": 0,
                    "false_positives": 0
                },
                "threat_categories": {},
                "language_distribution": {},
                "timestamp": datetime.utcnow().isoformat()
            }
        
        # Get total analyses
        total = await mongodb.analyses_collection.count_documents({})
        
        # Get high risk count
        high_risk = await mongodb.analyses_collection.count_documents({
            "$or": [
                {"risk_assessment.level": "HIGH"},
                {"risk_assessment.level": "CRITICAL"},
                {"combined_risk.level": "HIGH"},
                {"combined_risk.level": "CRITICAL"}
            ]
        })
        
        # Get reports generated (same as total for now)
        reports = total
        
        # Threat categories - count each type
        threat_categories = {}
        
        # Toxicity count
        toxic_count = await mongodb.analyses_collection.count_documents({
            "content_analysis.toxicity.is_toxic": True
        })
        if toxic_count > 0:
            threat_categories["Toxicity"] = toxic_count
        
        # Hate speech count
        hate_count = await mongodb.analyses_collection.count_documents({
            "content_analysis.hate_speech.is_hate_speech": True
        })
        if hate_count > 0:
            threat_categories["Hate Speech"] = hate_count
        
        # NSFW count
        nsfw_count = await mongodb.analyses_collection.count_documents({
            "content_analysis.nsfw.is_nsfw": True
        })
        if nsfw_count > 0:
            threat_categories["NSFW Content"] = nsfw_count
        
        # Misinformation count
        misinfo_count = await mongodb.analyses_collection.count_documents({
            "content_analysis.misinformation.is_misinformation": True
        })
        if misinfo_count > 0:
            threat_categories["Misinformation"] = misinfo_count
        
        # Language distribution
        language_dist = {}
        pipeline = [
            {"$match": {"language_analysis.detected_language": {"$exists": True, "$ne": None}}},
            {"$group": {"_id": "$language_analysis.detected_language", "count": {"$sum": 1}}}
        ]
        async for doc in mongodb.analyses_collection.aggregate(pipeline):
            if doc["_id"]:
                language_dist[doc["_id"]] = doc["count"]
        
        return {
            "daily_analysis": {
                "total_content_analyzed": total,
                "high_risk_detected": high_risk,
                "reports_generated": reports,
                "false_positives": 0
            },
            "threat_categories": threat_categories,
            "language_distribution": language_dist,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.error(f"Failed to get dashboard stats: {e}")
        return {
            "daily_analysis": {
                "total_content_analyzed": 0,
                "high_risk_detected": 0,
                "reports_generated": 0,
                "false_positives": 0
            },
            "threat_categories": {},
            "language_distribution": {},
            "timestamp": datetime.utcnow().isoformat()
        }