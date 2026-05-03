# FastAPI Learning Project

A full-stack application demonstrating FastAPI backend development with a React frontend. This project was built as a learning exercise to understand modern backend systems, database integration, and full-stack communication.

---

## Project Overview

This is a Product Management System designed primarily to learn and implement:

- FastAPI backend development from scratch
- Database integration using PostgreSQL and SQLAlchemy
- API design and data validation using Pydantic
- Cross-Origin Resource Sharing (CORS) handling
- Frontend–backend communication using REST APIs

The frontend was generated using AI assistance. The primary focus of this project is backend engineering, API design, and database interaction.

---

## Tech Stack

### Backend (Python)

| Technology | Purpose |
|-----------|---------|
| FastAPI | Web framework for building APIs |
| SQLAlchemy | ORM for database operations |
| Pydantic | Data validation and schema management |
| Uvicorn | ASGI server for running FastAPI |
| PostgreSQL | Relational database |
| psycopg2 | PostgreSQL adapter for Python |

### Frontend (React - AI Generated)

| Technology | Purpose |
|-----------|---------|
| React | UI library |
| Axios | HTTP client for API requests |
| React Scripts | Build and development tooling |

---

## Learning Objectives

The primary goal of this project was to master:

- FastAPI routing and request handling
- Dependency injection system in FastAPI
- PostgreSQL database integration
- SQLAlchemy ORM usage and model mapping
- Pydantic-based request and response validation
- CORS configuration for frontend-backend communication
- REST API design principles
- End-to-end data flow between frontend and backend

---

## FastAPI Concepts Implemented

### Route Handlers

```python
@app.get("/")
@app.get("/products")
@app.get("/products/{id}")
```

Defines API endpoints for handling HTTP requests.

### Dependency Injection

```python
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
```

Automatically manages database sessions and resource cleanup.

### CORS Configuration

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"]
)
```

Enables communication between frontend and backend running on different ports.

### Pydantic Validation

```python
class ProductSchema(BaseModel):
    id: int
    name: str
    price: int
    quantity: int
```

Ensures strict data validation for API requests and responses.

---

## Project Structure

```
PythonAPI/
├── main.py                 # FastAPI application and routes
├── models.py               # Pydantic schemas
├── database_models.py      # SQLAlchemy ORM models
├── database.py             # Database connection and session management
├── fastapi/                # Virtual environment
│   ├── bin/
│   ├── python
│   └── uvicorn
└── frontend/               # React application (AI generated)
    ├── package.json
    ├── public/
    └── src/
        ├── App.js
        ├── App.css
        └── components
```

---

## Data Flow Architecture

```
Frontend (React)
    ↓ HTTP Request (Axios)
FastAPI Backend
    ↓ Pydantic Validation
SQLAlchemy ORM
    ↓ SQL Query
PostgreSQL Database
    ↓ Response Data
SQLAlchemy ORM
    ↓ Python Objects
FastAPI Serialization
    ↓ JSON Response
Frontend UI Update
```

---

## Setup Instructions

### Prerequisites

- Python 3.12+
- PostgreSQL
- Node.js and npm

### Backend Setup

1. Navigate to project directory:
```bash
cd /home/aditya/Desktop/ARiES/PythonAPI
```

2. Activate virtual environment:
```bash
source fastapi/bin/activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary
```

4. Configure database connection in `database.py`:
```python
db_url = "postgresql://postgres:PASSWORD@localhost:5432/FastAPI-Testing"
```

5. Run backend server:
```bash
uvicorn main:app --reload
```

**API Documentation:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Frontend Setup

1. Navigate to frontend:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

Frontend runs at: http://localhost:3000

---

## API Endpoints

### Available Routes

```
GET /                → Base route
GET /products        → Fetch all products
GET /products/{id}   → Fetch product by ID
```

### Sample Response

```json
{
  "id": 1,
  "name": "phone",
  "description": "budget phone",
  "price": 9900,
  "quantity": 23
}
```

---

## Frontend Features (AI Generated)

- Product listing interface
- Search and filter functionality
- Sorting capabilities
- Add new products form
- Edit existing products
- Delete products
- Responsive UI layout

> **Note:** The frontend was generated using AI tools. The focus of this project is backend development and system integration.

---

## Key Backend Learnings

### FastAPI
- Route creation and HTTP method handling
- Dependency injection system
- Automatic API documentation
- Type-hint based validation

### Database Layer
- SQLAlchemy ORM modeling
- Session management
- CRUD operations
- Model mapping between Pydantic and SQLAlchemy

### API Integration
- RESTful design principles
- JSON serialization/deserialization
- Frontend-backend communication using Axios

### System Design
- Separation of concerns (routes, models, database)
- Clean architecture for scalability
- CORS handling for cross-origin requests

---

## Future Improvements

- [ ] Authentication system (JWT-based)
- [ ] Update (PUT/PATCH) API endpoints
- [ ] Pagination for product listing
- [ ] Centralized error handling
- [ ] Unit and integration tests
- [ ] Production deployment setup
- [ ] Redis caching layer

---

## References

- https://fastapi.tiangolo.com/
- https://docs.sqlalchemy.org/
- https://docs.pydantic.dev/
- https://react.dev/
- https://www.postgresql.org/docs/

---

## Author

**Aditya**

This project was created as a backend-focused learning exercise to understand FastAPI, PostgreSQL integration, and full-stack communication patterns.