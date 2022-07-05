from sqlalchemy.orm import Session
from datetime import datetime
import models
import schemas


def get_weather(db: Session):
    return db.query(models.Weather).all()


def get_weather_detail(db: Session, weather_id: int):
    return db.query(models.Weather).filter(models.Weather.id == weather_id).first()


def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.Weather(
        date=weather.date,
        hour=weather.hour,
        area=weather.area,
        temperature=weather.temperature,
        sky=weather.sky,
        humidity=weather.humidity,
        api_type=weather.api_type
    )
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def delete_weather(db: Session, weather_id: int):
    weather_delete = db.query(models.Weather).filter_by(id=weather_id).first()
    db.delete(weather_delete)
    db.commit()
    return True
