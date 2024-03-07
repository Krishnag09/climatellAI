from fastapi import FastAPI
from fastapi import APIRouter
from routers.users import router as user_router
from routers.weather_data import router as weather_router

router = APIRouter()

app = FastAPI()

app.include_router(user_router)
app.include_router(weather_router)
