from contextlib import asynccontextmanager

from fastapi import FastAPI


from app.api.auth import router as auth_router
from app.db.base import Base
from app.db.session import engine
from app.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Price Alerts API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Price Alerts API is running"}