from pydantic import BaseModel, Field, validator
from datetime import datetime


class NewsSchema(BaseModel):
    id: str
    title: str
    image: str
    url: str
    date: datetime
    processing_date: datetime


class NewsOrmSchema(BaseModel):
    title: str
    image_url: str = Field(alias="image")
    news_url: str = Field(alias="url")
    publication_date: datetime = Field(alias="date")

    @validator('publication_date')
    def date_transform(cls, value_date):
        return value_date.strftime("%Y-%m-%d")

    class Config:
        orm_mode = True

