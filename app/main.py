from fastapi import FastAPI
from app.database import init_db
from app.routers import health, tickets,attachments

app = FastAPI(
    title="CloudOps Helpdesk API",
    description="Beginner AWS practice project for EC2, Docker, CloudWatch, security groups, and API deployment.",
    version="0.1.0",
)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {
        "message": "CloudOps Helpdesk API is running",
        "docs": "/docs",
        "health": "/health",
    }

app.include_router(health.router)
app.include_router(tickets.router)
app.include_router(attachments.router)