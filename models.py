from sqlalchemy import Column, Integer, String, Float, Date, DateTime

from database import Base


class Weather(Base):
    __tablename__ = "weathers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    hour = Column(Integer)
    area = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    precipitation = Column(Integer)
    precipitation_amount = Column(Integer)
    sky = Column(String)
    api_type = Column(String)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)



