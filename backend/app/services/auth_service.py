from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest, UserCreate


def register_user(db: Session, user_data: UserCreate) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if existing_user:
        raise ValueError("Email is already registered")

    user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, credentials: LoginRequest) -> User | None:
    user = db.scalar(
        select(User).where(User.email == credentials.email)
    )
    if user is None or not verify_password(
        credentials.password,
        user.hashed_password,
    ):
        return None

    return user