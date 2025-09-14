from fastapi import APIRouter, HTTPException
import json

router = APIRouter(prefix="/users", tags=["users"])

database = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35}
}


@router.get('/')
async def get_all_users(): 
    return database

@router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    user = database.get(user_id)
    return user

@router.post('/')
async def create_user(user: dict):
    new_id = max(database.keys()) + 1
    database[new_id] = user
    return user

@router.delete('/{user_id}')
async def delete_user(user_id: int) -> str:
    database.pop(user_id, None)
    return "User Deleted"