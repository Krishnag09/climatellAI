from fastapi import APIRouter, HTTPException
import os
import httpx
from dotenv import load_dotenv


router = APIRouter()


load_dotenv()

weather_api_base_url = os.getenv("WEATHER_API_URL")
api_key = os.getenv("WEATHER_API_KEY")

weather_path = os.path.join(weather_api_base_url, "/data/2.5/forecast")


@router.get(weather_path, tags=["data"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/weather")
async def get_weather(lat: float, lon: float):
    params_body = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(weather_api_base_url, params=params_body)

        response.raise_for_status()
        print(response.json())
        return response.json()

    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=f"Request error occurred: {e}") from e
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail=f"Error response from OpenWeatherMap: {e}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred") from e
