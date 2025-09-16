from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from models.models import User
from beanie import init_beanie

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client['user_account']

app = FastAPI()

@app.on_event("startup")
async def app_init():
    # Initialize Beanie with the User document
    await init_beanie(database=db, document_models=[User])

def get_database() -> AsyncIOMotorClient:
    return db