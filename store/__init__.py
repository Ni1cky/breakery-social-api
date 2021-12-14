from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///users.db")
session_factory = sessionmaker(engine)
