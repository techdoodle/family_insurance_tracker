from fastapi import FastAPI
from contextlib import asynccontextmanager

from famsure.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan, title=settings.APP_NAME)

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}