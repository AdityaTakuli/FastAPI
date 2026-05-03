# 🚀 ARiES - FastAPI Learning Project

> A full-stack application demonstrating **FastAPI** backend development with a React frontend, built as a learning experience to master modern web technologies.

---

## 📚 Project Overview

This project is a **Product Management System** where:
- **Backend**: Built manually from scratch using **FastAPI** to learn core concepts
- **Frontend**: Styled with vibes using **React** for a smooth user experience
- **Database**: PostgreSQL for persistent data storage
- **Goal**: Master FastAPI, SQLAlchemy ORM, and full-stack development

---

## 🛠️ Tech Stack

### Backend (Python)

| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastAPI** | Modern, fast web framework for building APIs | 0.136.1 |
| **SQLAlchemy** | SQL toolkit & ORM for database operations | 2.0.49 |
| **Pydantic** | Data validation & settings management | 2.13.3 |
| **Uvicorn** | ASGI server to run FastAPI app | 0.46.0 |
| **PostgreSQL** | Relational database | - |
| **psycopg2** | PostgreSQL adapter for Python | 2.9.12 |

### Frontend (JavaScript/React)

| Technology | Purpose | Version |
|-----------|---------|---------|
| **React** | UI library for building components | 18.0.0 |
| **Axios** | HTTP client for API requests | 1.7.3 |
| **React Scripts** | Build tools for React apps | 5.0.1 |

---

## 🎓 FastAPI - What & Why?

### What is FastAPI?

FastAPI is a **modern Python framework** for building high-performance APIs. It's:
- ⚡ **Fast**: Auto-optimization, built on top of Starlette (fast ASGI framework)
- 📝 **Intuitive**: Clean syntax inspired by Python type hints
- 🔒 **Type-safe**: Full type hint support for better development experience
- 📖 **Auto-documented**: Automatic interactive API docs (Swagger UI, ReDoc)
- 🚀 **Production-ready**: Used in real-world applications

### Key FastAPI Concepts Used in This Project

#### 1️⃣ **Route Decorators**
```python
@app.get("/")           # GET endpoint
@app.get("/products")   # Fetch all products
@app.get("/products/{id}")  # Fetch product by ID
```
Routes map HTTP methods to Python functions.

#### 2️⃣ **Dependency Injection**
```python
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    # db is automatically injected
    return db.query(database_models.Product).all()
```
Cleaner code management, automatic resource cleanup.

#### 3️⃣ **CORS (Cross-Origin Resource Sharing)**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"]
)
```
Allows frontend (port 3000) to communicate with backend (port 8000).

#### 4️⃣ **Pydantic Validation**
```python
class ProductSchema(BaseModel):
    id: int
    name: str
    price: int
    quantity: int
```
Automatic request/response validation & documentation.

---

## 📁 Project Structure

```
PythonAPI/
├── main.py                 # FastAPI app, routes, CORS setup
├── models.py               # Pydantic schemas (request/response validation)
├── database_models.py      # SQLAlchemy models (database tables)
├── database.py             # Database connection & session management
├── fastapi/                # Virtual environment
│   └── bin/
│       ├── python         # Python interpreter
│       ├── uvicorn        # ASGI server
│       └── activate       # Activate venv
└── frontend/               # React application
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js          # Main React component
        ├── App.css         # Styling
        ├── TaglineSection.js
        └── index.js
```

---

## 🔄 How Data Flows

```
Frontend (React)
    ↓ (HTTP Request via Axios)
Backend (FastAPI)
    ↓ (Validates with Pydantic)
SQLAlchemy ORM
    ↓ (Converts to SQL)
PostgreSQL Database
    ↓ (Returns data)
SQLAlchemy ORM
    ↓ (Converts to Python objects)
Backend (FastAPI)
    ↓ (Serializes to JSON)
Frontend (React)
    ↓ (Updates state with data)
UI Rendered
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL
- Node.js & npm

### Backend Setup

1. **Navigate to project directory**
   ```bash
   cd /home/aditya/Desktop/ARiES/PythonAPI
   ```

2. **Activate virtual environment**
   ```bash
   source fastapi/bin/activate
   ```

3. **Install dependencies** (already in venv)
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary
   ```

4. **Configure database** (update in `database.py`)
   ```python
   db_url = "postgresql://postgres:PASSWORD@localhost:5432/FastAPI-Testing"
   ```

5. **Run FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
   - 📖 API Docs: `http://localhost:8000/docs`
   - 🎯 ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. **Navigate to frontend**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start React dev server**
   ```bash
   npm start
   ```
   - App: `http://localhost:3000`

---

## 📚 Key Learning Points

### What Was Learned

#### Backend (FastAPI)

✅ **Route Handlers** - Creating endpoints with `@app.get()`, `@app.post()`, etc.
✅ **Dependency Injection** - Injecting database sessions cleanly
✅ **Data Validation** - Using Pydantic for request/response schemas
✅ **CORS** - Enabling cross-origin requests for frontend communication
✅ **ORM Integration** - Connecting SQLAlchemy models to FastAPI endpoints
✅ **Type Hints** - Leveraging Python type hints for better IDE support

#### Database (SQLAlchemy + PostgreSQL)

✅ **Database Models** - Defining tables with SQLAlchemy declarative base
✅ **Sessions** - Managing database connections and transactions
✅ **Querying** - Filtering, retrieving, and manipulating data
✅ **Model Conversion** - Converting between Pydantic → Dict → SQLAlchemy

#### Frontend (React)

✅ **State Management** - Using `useState` for managing products, forms, filters
✅ **API Integration** - Axios for making HTTP requests to backend
✅ **Components** - Building reusable React components
✅ **Styling** - CSS for a vibrant, aesthetic UI

---

## 🔌 API Endpoints

### Implemented Endpoints

```
GET  /                     → Welcome message
GET  /products             → Fetch all products (with filtering/sorting)
GET  /products/{id}        → Fetch product by ID
```

### Example Request

```bash
curl http://localhost:8000/products/1
```

### Example Response

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

## 🎨 Frontend Features

- ✨ **Product List Display** - Beautiful table with all products
- 🔍 **Search & Filter** - Find products by name
- ↕️ **Sort** - Sort by any field (ascending/descending)
- ➕ **Add Products** - Form to add new products
- ✏️ **Edit Products** - Modify existing product details
- 🗑️ **Delete Products** - Remove products from inventory
- 📱 **Responsive Design** - Vibecoded styling for modern look

---

## 💡 Pydantic vs SQLAlchemy

### Pydantic (`models.py`)
- **Request/Response Validation** schemas
- Ensures data format before hitting database
- Provides automatic documentation

### SQLAlchemy (`database_models.py`)
- **Database Models** - actual table definitions
- ORM layer for database operations
- Can be queried and manipulated programmatically

### Conversion Flow
```python
ProductSchema (Pydantic)
    ↓ .model_dump() → Dictionary
    ↓
database_models.Product(**dict) → SQLAlchemy Object
    ↓ db.add() → Stored in database
```

---

## 🔐 CORS Explanation

**CORS Error**: Without `CORSMiddleware`, browser blocks frontend → backend requests (different ports)

**Solution**: Tell FastAPI to accept requests from frontend origin
```python
allow_origins=["http://localhost:3000"]  # Frontend's origin
```

---

## 🎯 Next Steps / Enhancements

- [ ] Add authentication (JWT tokens)
- [ ] Implement update (`PUT`/`PATCH`) endpoints
- [ ] Add pagination to product list
- [ ] Implement error handling
- [ ] Add unit tests
- [ ] Deploy to production
- [ ] Add caching with Redis

---

## 📝 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## 👨‍💻 Author

Built as a learning project by **Aditya** to master FastAPI and modern web development.

---

## 📄 License

This project is for learning purposes. Feel free to use and modify as needed.

---

**Happy Coding! 🚀**
