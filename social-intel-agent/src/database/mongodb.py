from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
import os
from datetime import datetime
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None
        self.analyses_collection = None
        self.statistics_collection = None
        self.cybercell_reports_collection = None
    
    async def connect(self):
        """Connect to MongoDB"""
        try:
            mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
            self.client = AsyncIOMotorClient(mongodb_uri)
            
            # Test connection
            await self.client.admin.command('ping')
            
            self.db = self.client.satya_drishti
            self.analyses_collection = self.db.analyses
            self.statistics_collection = self.db.statistics
            self.cybercell_reports_collection = self.db.cybercell_reports
            
            logger.info("Connected to MongoDB successfully")
            return True
        except ConnectionFailure as e:
            logger.error(f"MongoDB connection failed: {e}")
            return False
    
    async def disconnect(self):
        """Disconnect from MongoDB"""
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")
    
    async def save_analysis(self, analysis_data: dict):
        """Save analysis result to database"""
        try:
            analysis_data["created_at"] = datetime.utcnow()
            result = await self.analyses_collection.insert_one(analysis_data)
            logger.info(f"Analysis saved with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Failed to save analysis: {e}")
            return None
    
    async def get_analysis(self, analysis_id: str):
        """Get analysis by ID"""
        try:
            from bson import ObjectId
            result = await self.analyses_collection.find_one({"_id": ObjectId(analysis_id)})
            if result:
                result["_id"] = str(result["_id"])
            return result
        except Exception as e:
            logger.error(f"Failed to get analysis: {e}")
            return None
    
    async def get_statistics(self):
        """Get platform statistics"""
        try:
            total_analyses = await self.analyses_collection.count_documents({})
            
            # Risk level distribution
            pipeline = [
                {"$group": {"_id": "$risk_assessment.level", "count": {"$sum": 1}}}
            ]
            risk_distribution = {}
            async for doc in self.analyses_collection.aggregate(pipeline):
                risk_distribution[doc["_id"]] = doc["count"]
            
            # Platform breakdown
            pipeline = [
                {"$group": {"_id": "$platform", "count": {"$sum": 1}}}
            ]
            platform_breakdown = {}
            async for doc in self.analyses_collection.aggregate(pipeline):
                platform_breakdown[doc["_id"]] = doc["count"]
            
            return {
                "total_analyses": total_analyses,
                "risk_distribution": risk_distribution,
                "platform_breakdown": platform_breakdown
            }
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
            return {}

# Global MongoDB instance
mongodb = MongoDB()