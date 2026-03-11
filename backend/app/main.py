from fastapi import FastAPI

from app.api.routes import router
from app.core.database import Base, engine

app = FastAPI(title="ApexAds Autonomous AI Marketing OS", version="1.0.0")
Base.metadata.create_all(bind=engine)
app.include_router(router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
