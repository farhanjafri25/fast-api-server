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
    return database

@router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    return user_service.get_user_by_id(user_id)

@router.post('/')
async def create_user(user: UserCreate):
    return user_service.create_user(user)

    