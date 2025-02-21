from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models, routers

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI(
    title="Library API",
    description="A RESTful API for managing a collection of books",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routers.books.router)
app.include_router(routers.users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library API. Go to /docs for the API documentation."}