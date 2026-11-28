import os
from datetime import datetime, timedelta, timezone

from app.core.config import load_environment
from jose import JWTError, jwt
from pwdlib import PasswordHash

load_environment()

password_hash = PasswordHash.recommended()
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
) -> str:
    expires_at = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return jwt.encode(
        {"sub": subject, "exp": expires_at},
        _get_jwt_secret_key(),
        algorithm=JWT_ALGORITHM,
    )


def decode_access_token(token: str) -> str | None:
    try:
        claims = jwt.decode(
            token,
            _get_jwt_secret_key(),
            algorithms=[JWT_ALGORITHM],
            options={"require_exp": True, "require_sub": True},
        )
    except JWTError:
        return None

    subject = claims.get("sub")
    return subject if isinstance(subject, str) else None


def _get_jwt_secret_key() -> str:
    secret_key = os.getenv("JWT_SECRET_KEY")
    if not secret_key:
        raise RuntimeError("JWT_SECRET_KEY environment variable must be set")
    return secret_key