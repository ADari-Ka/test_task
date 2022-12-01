from fastapi import APIRouter
from service import change_data

sensors_handler = APIRouter()


@sensors_handler.post("/data")
async def post_data(data: dict):

    await change_data(data)

