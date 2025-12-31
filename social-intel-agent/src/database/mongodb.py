from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from datetime import datetime
import os

class MongoDB:
    def __init__(self):
        # MongoDB Atlas connection string
        self.connection_string = "mongodb+srv://AdminSD:onpDYSkRaDUjptrs@sd.fqozxem.mongodb.net/?appName=SD"
        self.client = None
        self.db = None
        
    async def connect(self):
        """Connect to MongoDB"""
        try:
            self.client = AsyncIOMotorClient(self.connection_string)
            self.db = self.client.satya_drishti
            # Test connection
            await self.client.admin.command('ping')
            print("✅ MongoDB Connected Successfully!")
            return True
        except Exception as e:
            print(f"❌ MongoDB Connection Failed: {e}")
            return False
    
    async def disconnect(self):
        """Disconnect from MongoDB"""
        if self.client:
            self.client.close()
            print("MongoDB Disconnected")
    
    # Analysis Results Collection
    async def save_analysis(self, analysis_data: dict):
        """Save analysis result to database"""
        try:
            collection = self.db.analysis_results
            analysis_data['created_at'] = datetime.utcnow()
            result = await collection.insert_one(analysis_data)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error saving analysis: {e}")
            return None
    
    async def get_analysis(self, analysis_id: str):
        """Get analysis by ID"""
        try:
            collection = self.db.analysis_results
            return await collection.find_one({"analysis_id": analysis_id})
        except Exception as e:
            print(f"Error getting analysis: {e}")
            return None
    
    async def get_recent_analyses(self, limit: int = 10):
        """Get recent analyses"""
        try:
            collection = self.db.analysis_results
            cursor = collection.find().sort("created_at", -1).limit(limit)
            return await cursor.to_list(length=limit)
        except Exception as e:
            print(f"Error getting recent analyses: {e}")
            return []
    
    # Statistics Collection
    async def update_stats(self, stats_data: dict):
        """Update governance statistics"""
        try:
            collection = self.db.governance_stats
            stats_data['updated_at'] = datetime.utcnow()
            
            # Upsert (update or insert)
            await collection.update_one(
                {"_id": "global_stats"},
                {"$set": stats_data},
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Error updating stats: {e}")
            return False
    
    async def get_stats(self):
        """Get governance statistics"""
        try:
            collection = self.db.governance_stats
            stats = await collection.find_one({"_id": "global_stats"})
            if not stats:
                # Initialize default stats
                default_stats = {
                    "_id": "global_stats",
                    "total_analyzed": 0,
                    "high_risk_detected": 0,
                    "reports_generated": 0,
                    "by_category": {},
                    "by_language": {},
                    "updated_at": datetime.utcnow()
                }
                await collection.insert_one(default_stats)
                return default_stats
            return stats
        except Exception as e:
            print(f"Error getting stats: {e}")
            return None
    
    async def increment_stat(self, field: str, value: int = 1):
        """Increment a specific stat"""
        try:
            collection = self.db.governance_stats
            await collection.update_one(
                {"_id": "global_stats"},
                {"$inc": {field: value}, "$set": {"updated_at": datetime.utcnow()}},
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Error incrementing stat: {e}")
            return False
    
    # Cybercell Reports Collection
    async def save_report(self, report_data: dict):
        """Save cybercell report"""
        try:
            collection = self.db.cybercell_reports
            report_data['created_at'] = datetime.utcnow()
            result = await collection.insert_one(report_data)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error saving report: {e}")
            return None
    
    async def get_report(self, report_id: str):
        """Get report by ID"""
        try:
            collection = self.db.cybercell_reports
            return await collection.find_one({"report_id": report_id})
        except Exception as e:
            print(f"Error getting report: {e}")
            return None
    
    async def get_reports_by_severity(self, severity: str, limit: int = 10):
        """Get reports by severity level"""
        try:
            collection = self.db.cybercell_reports
            cursor = collection.find({"severity": severity}).sort("created_at", -1).limit(limit)
            return await cursor.to_list(length=limit)
        except Exception as e:
            print(f"Error getting reports: {e}")
            return []
    
    # Source Verification Cache
    async def cache_source_verification(self, url: str, verification_data: dict):
        """Cache source verification result"""
        try:
            collection = self.db.source_cache
            verification_data['url'] = url
            verification_data['cached_at'] = datetime.utcnow()
            
            await collection.update_one(
                {"url": url},
                {"$set": verification_data},
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Error caching verification: {e}")
            return False
    
    async def get_cached_verification(self, url: str):
        """Get cached source verification"""
        try:
            collection = self.db.source_cache
            return await collection.find_one({"url": url})
        except Exception as e:
            print(f"Error getting cached verification: {e}")
            return None

# Global MongoDB instance
mongodb = MongoDB()
