import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
path = os.environ.get('DATABASE', "sqlite:///database.db")
engine = create_engine(path)
session_factory = sessionmaker(engine)

