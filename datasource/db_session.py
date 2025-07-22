from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .configuration import Config

engine=create_engine(Config.SQLALCHEMY_DATABASE_URI)
local_session=sessionmaker(bind=engine)
