# Price Alerts — Implementation Guide

This guide covers the current local development setup. The backend authentication API exists; product monitoring and notification workflows are still planned.

## Prerequisites

- Python 3.12 recommended
- PostgreSQL running locally or reachable through a connection URL
- Node.js and npm for the Vue frontend

## 1. Create and activate a Python environment

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
```

In macOS/Linux shells, activate with:

```sh
source .venv/bin/activate
```

## 2. Configure the backend

Create `backend/.env` locally. Do not commit it. The configuration loader reads this file from the backend directory.

```dotenv
DATABASE_URL=postgresql+psycopg://<username>:<password>@localhost:5432/price_alerts
JWT_SECRET_KEY=<generate-a-unique-random-value>
```

Generate a JWT secret locally, then paste the generated output into `.env`:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Replace the database URL placeholders with credentials for your local PostgreSQL instance. The database itself must exist before starting the API; the application creates its tables at startup.

## 3. Start the backend

From the repository root:

```powershell
Set-Location backend
uvicorn app.main:app --reload
```

The API base URL is `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`. The backend allows the local Vite origins by default; set `FRONTEND_ORIGINS` to a comma-separated list when serving the frontend from another origin.

### Current authentication endpoints

Register:

```http
POST /api/v1/auth/register
Content-Type: application/json
```

```json
{
  "email": "shopper@example.com",
  "password": "a-local-test-password"
}
```

Login:

```http
POST /api/v1/auth/login
Content-Type: application/json
```

```json
{
  "email": "shopper@example.com",
  "password": "a-local-test-password"
}
```

Successful login returns an `access_token` and `token_type`. The frontend registration and sign-in forms use these endpoints; after registration, the form flips to sign in.

## 4. Run backend tests

From the `backend` directory:

```powershell
python -m pytest tests -q
```

## 5. Start the frontend

In a second terminal:

```powershell
Set-Location frontend
npm install
npm run dev
```

Vite prints the local frontend URL when it starts. The authentication form uses `http://127.0.0.1:8000` by default; set `VITE_API_BASE_URL` when the API is hosted elsewhere.

## Troubleshooting

- **`DATABASE_URL environment variable must be set`:** check that `backend/.env` exists and contains a valid `DATABASE_URL`.
- **Database connection error:** make sure PostgreSQL is running, the database exists, and the URL credentials are correct.
- **`JWT_SECRET_KEY environment variable must be set`:** check that `backend/.env` contains a non-empty `JWT_SECRET_KEY`, then restart the backend.
- **Do not commit `.env`:** it contains local credentials and must remain ignored by Git.
