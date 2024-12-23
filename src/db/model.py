from sqlalchemy import Column, Integer, Float, Enum, String

from src.db.core import Base, engine
from src.config import db_config
from src.schemas.events import Status


class Events(Base):
    __tablename__ = db_config.db_table_name

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    coefficient = Column(Float)
    timestamp = Column(Integer)
    status = Column(Enum(Status))


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
