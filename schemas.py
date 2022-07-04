from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field


class WeatherBase(BaseModel):
    date: date
    hour: int
    area: str
    temperature: float
    sky: str
    created_at: datetime
    updated_at: datetime


class Weather(WeatherBase):
    class Config:
        id: int
        orm_mode = True
