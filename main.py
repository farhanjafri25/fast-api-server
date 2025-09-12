from fastapi import FastAPI
from api.routes.user_routes import router as user_router

app = FastAPI()

@app.get('/')
async def hello(): 
    return {"message": "Hello, world"}

app.include_router(user_router)

