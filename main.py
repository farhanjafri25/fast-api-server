from fastapi import FastAPI
from api.routes.user_routes import router as user_router
from response_middleware import ResponseWrapperMiddleware

app = FastAPI()

@app.get('/')
async def hello(): 
    return {"message": "Hello, world"}

app.include_router(user_router)

app.add_middleware(
    ResponseWrapperMiddleware
)