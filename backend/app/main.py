from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import auth, files, flashcards, podcast
from .core.config import settings
from .core.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LearnLab API",
    description="Backend API for LearnLab application",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    files.router,
    prefix="/api/files",
    tags=["Files"]
)

app.include_router(
    flashcards.router,
    prefix="/api/flashcards",
    tags=["Flashcards"]
)

app.include_router(
    podcast.podcast_router,
    prefix="/api/podcasts",
    tags=["Podcasts"]
)

app.include_router(
    podcast.progress_router,
    prefix="/api/podcasts",
    tags=["Podcast Progress"]
)

app.include_router(
    podcast.analytics_router,
    prefix="/api/podcasts",
    tags=["Podcast Analytics"]
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to LearnLab API",
        "documentation": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Service is running"
    }