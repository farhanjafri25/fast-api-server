from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    username: str
    user_id: str
    email: EmailStr
    is_active: bool
    full_name: str | None = None