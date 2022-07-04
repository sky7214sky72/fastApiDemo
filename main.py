from enum import Enum
from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.Weather])
def read_weather(db: Session = Depends(get_db)):
    weathers = crud.get_weather(db)
    return weathers


@app.get("/weather/{weather_id}", response_model=schemas.Weather)
def read_weather_detail(weather_id: int, db: Session = Depends(get_db)):
    weather = crud.get_weather_detail(db, weather_id)
    return weather

