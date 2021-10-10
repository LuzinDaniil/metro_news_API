from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .base import metadata

Base = declarative_base(metadata=metadata)


class NewsModel(Base):
    __tablename__ = 'news_table'
    id = Column(String(36), primary_key=True, nullable=False)
    title = Column(Text, unique=True)
    image = Column(Text)
    url = Column(Text)
    date = Column(DateTime)
    processing_date = Column(DateTime)
