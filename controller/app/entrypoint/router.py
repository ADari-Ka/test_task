from fastapi import APIRouter
from service import change_data
from model.sensor_data import SensorData

sensors_handler = APIRouter()


@sensors_handler.post("/data")
async def post_data(data: SensorData):

    await change_data(data)

