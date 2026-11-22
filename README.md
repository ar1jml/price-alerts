# Price Alerts — Intelligent Price Monitoring System

An asynchronous price-monitoring backend that tracks products across online stores, records historical prices, and automatically notifies users when products reach their target prices.

Built with Python, FastAPI, PostgreSQL, Redis, and Celery, with a focus on reliable background processing, scalable architecture, and maintainable backend design.

---

## Overview

Price Alerts allows users to monitor products from supported online stores without manually checking prices.

Users can register products, define price thresholds, and receive notifications when prices change or reach their desired target.

The system runs price-checking jobs asynchronously, stores historical price data, evaluates alert conditions, and dispatches notifications through a background processing pipeline.

## Core Features

### Authentication & Authorization
- User registration and login
- Secure password hashing
- JWT authentication
- Access token and refresh token management
- Protected API endpoints
- User-level resource ownership

### Product Monitoring
- Track products from supported online stores
- Extract product names and prices
- Monitor product availability
- Normalize prices and currencies
- Store current product prices

### Price Tracking
- Historical price records
- Price change detection
- Lowest and highest recorded prices
- Price trend analysis
- Price-drop percentage calculation

### Alert Management
- User-defined target prices
- Price-drop conditions
- Automated alert evaluation
- Notification cooldowns
- Duplicate alert prevention
- Alert activation and deactivation

### Background Processing
- Asynchronous price-checking jobs
- Distributed task processing
- Scheduled price monitoring
- Automatic retries
- Task timeouts
- Failure handling

### Notifications
- Email notifications
- Notification history
- Delivery status tracking
- Retry failed notifications

---

## Architecture

The system uses a modular backend architecture with separate responsibilities for API requests, business logic, data persistence, background processing, and external integrations.

```mermaid
flowchart TD
    A[Client Application] --> B[FastAPI]
    B --> C[Authentication & Authorization]
    B --> D[Application Services]
    D --> E[(PostgreSQL)]
    D --> F[Redis]
    F --> G[Celery Workers]
    H[Celery Beat] --> F
    G --> I[Store Price Extraction]
    I --> J[External Stores]
    G --> K[Price Processing]
    K --> E
    K --> L[Alert Evaluation]
    L --> F
    F --> M[Notification Worker]
    M --> N[Email Provider]
```

### Components

| Component | Responsibility |
|---|---|
| FastAPI | HTTP endpoints, validation, request handling |
| PostgreSQL | Persistent application data |
| SQLAlchemy | Database interaction and ORM |
| Alembic | Database schema migrations |
| Redis | Message broker and caching |
| Celery | Background task execution |
| Celery Beat | Periodic task scheduling |
| HTTPX | Asynchronous HTTP communication |
| Pydantic | Data validation and serialization |
| Pytest | Automated testing |
| Docker | Containerized development and deployment |

---

## Price Monitoring Workflow

1. A user registers and authenticates.
2. The user submits a product URL and target price.
3. The API validates the request and stores the tracking configuration.
4. A monitoring job is scheduled or queued.
5. A worker retrieves the product's current price.
6. The extracted data is validated and normalized.
7. The current price and historical record are updated.
8. The alert engine evaluates the user's conditions.
9. A notification task is queued when an alert condition is satisfied.
10. The notification worker sends the email and records the delivery result.

---

## Technology Stack

### Backend
- Python
- FastAPI
- Pydantic

### Database
- PostgreSQL
- SQLAlchemy 2.0
- Alembic

### Background Processing
- Redis
- Celery
- Celery Beat

### HTTP & Data Extraction
- HTTPX
- BeautifulSoup

### Security
- JWT
- Password hashing
- Authorization and ownership checks

### Testing & DevOps
- Pytest
- Docker
- Docker Compose
- GitHub Actions

---

## Database Entities

The database is designed around the following entities:

| Entity | Description |
|---|---|
| Users | Registered users and authentication data |
| Stores | Supported online stores |
| Products | Product information and current prices |
| Tracked Products | User-to-product tracking relationships |
| Price Alerts | User-defined alert conditions |
| Price History | Historical price records |
| Notifications | Notification attempts and delivery statuses |

---

## API Modules

The API is organized into versioned modules.

| Module | Responsibility |
|---|---|
| Authentication | Registration, login, token management |
| Users | User account management |
| Products | Product tracking and management |
| Alerts | Price alert configuration |
| Price History | Historical pricing information |
| Notifications | Notification status and history |

API documentation will be available through Swagger UI and ReDoc.

---

## Project Structure

```text
price-alerts/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       └── router.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── workers/
│   ├── scrapers/
│   └── main.py
├── tests/
├── alembic/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── .env.example
└── README.md
```

---

## Development Setup

### Prerequisites

- Python 3.12+
- Docker
- Docker Compose
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/price-alerts.git
cd price-alerts
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> Installation instructions will be finalized as the project configuration is implemented.

### Environment Variables

Create a `.env` file in the project root.

```env
APP_NAME=Price Alerts
ENVIRONMENT=development
SECRET_KEY=replace_with_secure_secret

DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/price_alerts

REDIS_URL=redis://localhost:6379/0

ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

SMTP_HOST=
SMTP_PORT=
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM_EMAIL=
```

Never commit real secrets, passwords, API keys, or production environment variables.

---

## Testing

The project uses Pytest for unit, integration, and API testing.

```bash
pytest
```

Tests will cover:

- Authentication and token handling
- API validation
- Product ownership
- Database operations
- Price extraction
- Alert evaluation
- Background task behavior
- Notification processing
- Error handling

---

## Engineering Goals

This project is intended to explore and demonstrate:

- Modular backend architecture
- REST API design
- Database relationships and transaction management
- Asynchronous processing
- Distributed background tasks
- Reliability and retry strategies
- Idempotency
- Data validation
- Authentication and authorization
- Automated testing
- Containerized deployment

---

## Roadmap

- [ ] Project architecture and configuration
- [ ] PostgreSQL setup
- [ ] SQLAlchemy models
- [ ] Alembic migrations
- [ ] Authentication and authorization
- [ ] Product management API
- [ ] Store integration and price extraction
- [ ] Price history
- [ ] Alert engine
- [ ] Redis integration
- [ ] Celery workers
- [ ] Scheduled price monitoring
- [ ] Email notifications
- [ ] Retry and failure handling
- [ ] Testing
- [ ] Dockerized deployment
- [ ] CI/CD pipeline
- [ ] Production deployment

---

## Project Status

**Status:** In Development

This project is being developed incrementally, starting with the core backend and progressing toward an asynchronous, distributed price-monitoring system.

---

## License

This project is intended for educational and portfolio purposes. A license will be added when the repository is prepared for public distribution.
