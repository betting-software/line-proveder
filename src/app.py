from fastapi import FastAPI

from src.api.events import router as events_router


app = FastAPI(
    title="LINE PROVIDER API",
    description="API for work with events db",
    version="1.0.0",
)


app.include_router(events_router)
