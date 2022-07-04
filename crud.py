from sqlalchemy.orm import Session
from datetime import datetime
import models
import schemas


def get_weather(db: Session):
    return db.query(models.Weather).all()


def get_weather_detail(db: Session, weather_id: int):
    return db.query(models.Weather).filter(models.Weather.id == weather_id).first()
