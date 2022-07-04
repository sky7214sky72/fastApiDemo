from sqlalchemy.orm import Session

import models


def get_weather(db: Session):
    return db.query(models.Weather).all()
