from types import SimpleNamespace

import pytest
from jose import jwt

from app.core.security import (
    JWT_ALGORITHM,
    create_access_token,
    hash_password,
)
from app.schemas.auth import LoginRequest
from app.services.auth_service import authenticate_user


class StubSession:
    def __init__(self, user):
        self.user = user

    def scalar(self, statement):
        return self.user


def test_authenticate_user_accepts_matching_password():
    user = SimpleNamespace(
        email="shopper@example.com",
        hashed_password=hash_password("correct-password"),
    )

    result = authenticate_user(
        StubSession(user),
        LoginRequest(email=user.email, password="correct-password"),
    )

    assert result is user


def test_authenticate_user_rejects_wrong_password():
    user = SimpleNamespace(
        email="shopper@example.com",
        hashed_password=hash_password("correct-password"),
    )

    result = authenticate_user(
        StubSession(user),
        LoginRequest(email=user.email, password="wrong-password"),
    )

    assert result is None


def test_create_access_token_contains_user_id_and_expiry(monkeypatch):
    secret = "test-secret-key-for-jwt-signing"
    monkeypatch.setenv("JWT_SECRET_KEY", secret)

    token = create_access_token("42")
    claims = jwt.decode(token, secret, algorithms=[JWT_ALGORITHM])

    assert claims["sub"] == "42"
    assert isinstance(claims["exp"], int)


def test_create_access_token_requires_secret(monkeypatch):
    monkeypatch.delenv("JWT_SECRET_KEY", raising=False)

    with pytest.raises(RuntimeError, match="JWT_SECRET_KEY"):
        create_access_token("42")
