from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
os.environ.get('DATABASE', "sqlite:///database.db")
engine = create_engine("sqlite:///database.db")
session_factory = sessionmaker(engine)
