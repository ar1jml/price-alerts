from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from jose import jwt

from app.api.auth import get_current_user
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

    def get(self, model, identity):
        if self.user is not None and self.user.id == identity:
            return self.user
        return None


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


def test_get_current_user_accepts_valid_bearer_token(monkeypatch):
    monkeypatch.setenv("JWT_SECRET_KEY", "test-secret-key-for-jwt-signing")
    user = SimpleNamespace(id=42, email="shopper@example.com")
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials=create_access_token(str(user.id)),
    )

    result = get_current_user(credentials, StubSession(user))

    assert result is user


@pytest.mark.parametrize(
    "credentials",
    [
        None,
        HTTPAuthorizationCredentials(
            scheme="Bearer",
            credentials="not-a-valid-token",
        ),
    ],
)
def test_get_current_user_rejects_missing_or_invalid_token(
    monkeypatch,
    credentials,
):
    monkeypatch.setenv("JWT_SECRET_KEY", "test-secret-key-for-jwt-signing")

    with pytest.raises(HTTPException) as error:
        get_current_user(credentials, StubSession(None))

    assert error.value.status_code == 401
    assert error.value.headers == {"WWW-Authenticate": "Bearer"}


def test_get_current_user_rejects_unknown_user(monkeypatch):
    monkeypatch.setenv("JWT_SECRET_KEY", "test-secret-key-for-jwt-signing")
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials=create_access_token("42"),
    )

    with pytest.raises(HTTPException) as error:
        get_current_user(credentials, StubSession(None))

    assert error.value.status_code == 401
