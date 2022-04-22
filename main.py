from handler.order_handler import router
from fastapi import FastAPI, APIRouter

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "hello world"}