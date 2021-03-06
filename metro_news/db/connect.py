from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('sqlite:///metro_news/db.sqlite')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
