# FastAPI Backend – Auth, Profiles, Posts

Production-ready FastAPI backend with JWT authentication, user profiles, and post management.  
Runs in Docker behind Nginx with PostgreSQL as the database.

Built with clean separation between API layer, business logic, and data layer.

---

## Tech Stack

- FastAPI  
- PostgreSQL 15  
- SQLAlchemy ORM  
- Alembic (migrations)  
- Docker + Docker Compose  
- Nginx (reverse proxy)  
- Gunicorn + Uvicorn workers  
- JWT (RSA) authentication  

---

## Project Structure

app/
api_routers/ -> API endpoints
orm_models/ -> SQLAlchemy models
schemas/ -> Pydantic schemas
services/ -> Business logic
db/ -> DB session & engine
core/ -> Config, security, startup
validation/ -> Custom validators

alembic/ -> Migrations
tests/ -> Test suite

yaml
Copy code

Layering:
- Routers handle HTTP
- Services handle logic
- Models handle DB

---

## Request Flow

Client → Nginx → Gunicorn → FastAPI → Router → Service → DB → Response

yaml
Copy code

- Nginx receives and forwards traffic  
- Gunicorn manages workers  
- FastAPI handles routing and validation  
- Services contain business logic  
- ORM models talk to PostgreSQL  

---

## Authentication

- JWT using RSA public/private keys  
- Passwords hashed with bcrypt + pepper  
- Dependency-based route protection  
- Fully stateless (no sessions)

---

## Database

- PostgreSQL 15  
- SQLAlchemy ORM  
- Connection pooling enabled  
- Alembic for schema migrations  

---

## Environment Variables

DATA_BASE -> PostgreSQL connection string
ALGORITHM -> JWT algorithm (RS256)
PRIVATE_KEY -> JWT signing key
PUBLIC_KEY -> JWT verification key
PEPPER_PASS -> Extra password security

yaml
Copy code

---

## API Endpoints

### Auth
- POST /user/signup  
- POST /user/login  

### Profile
- POST /profile/create  
- GET  /profile/view/{username}  

### Posts
- POST /posts/create  
- GET  /posts/view  

---

## Docker Setup

- App runs in its own container  
- PostgreSQL runs in separate container  
- Nginx sits in front as reverse proxy  
- All services wired using docker-compose  

Run locally:

```bash
docker-compose up --build
Nginx + Gunicorn
Nginx handles:

SSL termination

Reverse proxy

Request forwarding

Gunicorn runs multiple Uvicorn workers

Gunicorn is not exposed directly to the internet

Testing
bash
Copy code
pytest
Covers:

Auth

Profile

Posts

Error cases

Design Decisions
FastAPI → async, type-safe, clean routing

Service layer → keeps routers thin

Docker → consistent environment

Nginx → production-grade traffic handling

JWT (RSA) → secure, scalable auth

What This Project Demonstrates
Clean backend architecture

Real authentication flow

Proper Docker + Nginx setup

Production-style structure

Security-aware design

yaml
Copy code

---

### Why this version is **interviewer-grade**

- No AI tone  
- No fluff  
- No over-explaining  
- Clean sections  
- Easy to skim  
- Looks like written by a backend engineer, not a student

---

Next level (highly recommended):
👉 I can now rewrite this **even tighter for GitHub profile impact**  
👉 Or write a **killer 3-line project summary for resume/LinkedIn**

Just tell me what you want next.