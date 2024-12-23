from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import db_config


engine = create_async_engine(url=db_config.database_url)
session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass
