from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import analyze, health, image_analyze, governance
from src.database.mongodb import mongodb
from src.config.logger import setup_logger

app = FastAPI(
    title="Social Intelligence Agent",
    version="1.0.0"
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
    return {"message": "Social Intelligence Agent API is running"}

# Routers
app.include_router(analyze.router)
app.include_router(image_analyze.router)
app.include_router(health.router)
app.include_router(governance.router)

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Social Intelligence Agent started")
    await mongodb.connect()

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Social Intelligence Agent shutting down")
    await mongodb.disconnect()
