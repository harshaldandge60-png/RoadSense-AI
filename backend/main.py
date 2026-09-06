from fastapi import FastAPI

app = FastAPI(
    title="RoadSense AI API",
    description="Backend API for the RoadSense AI road monitoring system.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "RoadSense AI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
from fastapi import FastAPI

app = FastAPI(
    title="RoadSense AI API",
    description="Backend API for the RoadSense AI road monitoring system.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "RoadSense AI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    } 