from db_connection import db
from schemas.schemas import UserCreate, UserRead
from models.models import User
from passlib.hash import bcrypt

class UserService:
    def __init__(self):
        self.collection = db['users']


    async def create_user(self, user: UserCreate):
        user_dict = user.dict()
        user_dict['hashed_password'] = bcrypt.hash(user_dict.pop('password'))
        new_user = User(**user_dict)
        await new_user.insert()
        return UserRead(**new_user.dict())

    async def get_user_by_id(user_id: str):
        user = await User.get(user_id)
        if user:
            return UserRead(**user.dict())
        return None
