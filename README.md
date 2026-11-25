# Price Alerts

### Automated Price Tracking & Savings

Help shoppers track product prices, understand price changes, and decide when an item is worth buying.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue](https://img.shields.io/badge/Frontend-Vue%203-4FC08D?logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

Price Alerts is an early-stage price-tracking application. The goal is to help shoppers monitor products and get notified when prices reach a target they choose.

### Current implementation

- Backend user registration and login endpoints
- Password hashing and JWT access-token creation
- Vue 3/Vite dashboard interface prototype
- PostgreSQL user model and backend tests

The frontend is not yet connected to the authentication API. Product monitoring, price history, scheduled checks, and notifications are planned work, not implemented features.

## Product direction

The intended user journey is:

1. Add a product page URL and desired price.
2. Record price checks over time.
3. Notify the user when a tracked product reaches the desired price.

## Technology

| Area | Technology |
| --- | --- |
| Frontend | Vue 3, Vite, Vue Router |
| Backend API | Python, FastAPI |
| Data access | SQLAlchemy |
| Database | PostgreSQL |
| Authentication | `pwdlib` password hashing, JWT access tokens |
| Tests | Pytest |

## Quick start

See the [Implementation Guide](./Implementation_Guide.md) for environment setup, backend and frontend commands, and API examples.

The backend requires a local `backend/.env` file containing `DATABASE_URL` and `JWT_SECRET_KEY`. Keep that file private; it is ignored by Git.

## Documentation

- [PRD.md](./PRD.md) — Product goals, requirements, and planned scope
- [Implementation_Guide.md](./Implementation_Guide.md) — Setup, running, and testing the project
- [Technical_Architecture.md](./Technical_Architecture.md) — Current system design and implementation boundaries

## License

The project declares the MIT License.

---

Built by Arafat J. | Python Backend Developer
