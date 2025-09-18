from fastapi import APIRouter, HTTPException
import json
from schemas.schemas import UserCreate, UserRead
from services.user_service import UserService
from typing import List
from fastapi.responses import JSONResponse

user_service = UserService()

router = APIRouter(prefix="/users", tags=["users"])


@router.get('/')
async def get_all_users(): 
    # return database
    pass

@router.get('/{user_id}')
async def get_user(user_id: int):
    user = await user_service.get_user_by_id(user_id)


@router.post('/')
async def create_user(user: UserCreate):
    print(f"user: {user}")
    return await user_service.create_user(user=user)

    