from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.database.mongodb import mongodb
from src.config.logger import setup_logger

logger = setup_logger(__name__)
router = APIRouter()

class AnalysisQuery(BaseModel):
    analysis_id: str

@router.get("/analysis/{analysis_id}")
async def get_analysis(analysis_id: str):
    """Get analysis by ID"""
    try:
        result = await mongodb.get_analysis(analysis_id)
        if not result:
            raise HTTPException(status_code=404, detail="Analysis not found")
        return result
    except Exception as e:
        logger.error(f"Failed to get analysis: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/statistics/")
async def get_statistics():
    """Get platform statistics"""
    try:
        stats = await mongodb.get_statistics()
        return stats
    except Exception as e:
        logger.error(f"Failed to get statistics: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")