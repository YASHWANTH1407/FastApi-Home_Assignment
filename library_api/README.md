 Library API

A FastAPI-based RESTful API for managing a collection of books. This project implements CRUD operations for books with validation, error handling, and JWT authentication.

## Features

- FastAPI framework with organized routers
- SQLite database with SQLAlchemy ORM
- Book management (CRUD operations)
- User authentication using JWT tokens
- Input validation and error handling
- API documentation with Swagger UI

## Project Structure

```
library_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routers/
│       ├── __init__.py
│       ├── books.py
│       └── users.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/library-api.git
   cd library-api
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the API server:
   ```
   uvicorn app.main:app --reload
   ```

2. The API will be available at http://127.0.0.1:8000
3. API documentation can be accessed at http://127.0.0.1:8000/docs

## API Endpoints

### Book Endpoints

- `GET /books/` - Get all books
- `GET /books/{book_id}` - Get a specific book
- `POST /books/` - Create a new book (requires authentication)
- `PUT /books/{book_id}` - Update a book (requires authentication)
- `DELETE /books/{book_id}` - Delete a book (requires authentication)