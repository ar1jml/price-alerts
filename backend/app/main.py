from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.api.v1.auth import router as auth_router
from app.core.dependencies import get_current_user, require_role
from app.models.user import User
from app.schemas.user import UserResponse


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)


app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "PriceTrack API is running"
    }


@app.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }


@app.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user


@app.get("/admin-test")
def admin_test(
    current_user: User = Depends(require_role("admin")),
):
    return {
        "message": "You are an admin",
        "user": current_user.name,
    }