from pydantic import BaseModel, Field, constr, EmailStr
from typing import Optional, List

# Book schemas
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, example="The Great Gatsby")
    author: str = Field(..., min_length=1, example="F. Scott Fitzgerald")
    published_year: int = Field(..., gt=0, lt=10000, example=1925)
    isbn: constr(strict=True, min_length=10, max_length=13) = Field(example="9780743273565")  # type: ignore # Fixed


class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, example="The Great Gatsby")
    author: Optional[str] = Field(None, min_length=1, example="F. Scott Fitzgerald")
    published_year: Optional[int] = Field(None, gt=0, lt=10000, example=1925)
    isbn: Optional[constr(strict=True, min_length=10, max_length=13)] = Field(example="9780743273565")  # type: ignore # Fixed

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None