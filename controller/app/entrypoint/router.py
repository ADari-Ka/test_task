from fastapi import APIRouter

sensors_handler = APIRouter()


@sensors_handler.post("/data")
async def post_data():
    return {"message": "Hello World"}
