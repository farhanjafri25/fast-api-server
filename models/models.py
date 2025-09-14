from beanie import Document
from pydantic import EmailStr
from typing import Optional

class User(Document):
    username: str
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    full_name: Optional[str] = None

    class Settings:
        name = "users"  # Collection name in MongoDB
        indexes = ["email"]  # Example index on email field