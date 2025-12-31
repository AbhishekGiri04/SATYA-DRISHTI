from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import analyze, health, image_analyze, governance
from src.config.logger import setup_logger
from src.database.mongodb import mongodb

app = FastAPI(
    title="SATYA-DRISHTI - Digital Suraksha Framework",
    version="2.0.0",
    description="AI-Powered Content Moderation by Abhishek Giri"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# Logger
logger = setup_logger(__name__)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "SATYA-DRISHTI API is running",
        "developer": "Abhishek Giri",
        "github": "https://github.com/abhishekgiri04"
    }

# Routers
app.include_router(analyze.router)
app.include_router(image_analyze.router)
app.include_router(health.router)
app.include_router(governance.router)

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("SATYA-DRISHTI started - Developed by Abhishek Giri")
    # Connect to MongoDB
    await mongodb.connect()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("SATYA-DRISHTI shutting down")
    # Disconnect from MongoDB
    await mongodb.disconnect()
