from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.settings import SETTINGS
from pydantic import BaseModel
from typing import Literal
from pathlib import Path
from fastapi import APIRouter, HTTPException
import numpy as np
import joblib

router = APIRouter()
model = joblib.load("app/utils/model.pkl")


class RideData(BaseModel):
    Number_of_Riders: int
    Number_of_Drivers: int
    Location_Category: str
    Customer_Loyalty_Status: str
    Number_of_Past_Rides: int
    Average_Ratings: float
    Time_of_Booking: str
    Vehicle_Type: str
    Expected_Ride_Duration: int
    Historical_Cost_of_Ride: float


def preprocess_ride_data(vehicle: str, location: str) -> tuple[int, int]:
    vehicle_order = {"Economy": 0, "Premium": 1}
    location_order = {"Urban": 0, "Suburban": 1, "Rural": 2}

    vehicle_code = vehicle_order.get(vehicle)
    location_code = location_order.get(location)

    if vehicle_code is None or location_code is None:
        raise ValueError(f"Unknown category: vehicle={vehicle}, location={location}")

    return vehicle_code, location_code


@router.post("/predict")
async def predict_cost(features: RideData):

    vehicle_code, location_code = preprocess_ride_data(
        vehicle=features.Vehicle_Type, location=features.Location_Category
    )

    input_vector = np.array(
        [[location_code, vehicle_code, features.Expected_Ride_Duration]]
    )
    prediction = model.predict(input_vector)

    return JSONResponse(
        status_code=200, content={"predicted_price": float(prediction[0])}
    )
