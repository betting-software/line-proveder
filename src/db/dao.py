from typing import TypeVar, Generic
from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError

from src.db.core import session
from src.db.model import Events


ModelType = TypeVar('ModelType')


class BaseDAO(Generic[ModelType]):
    model: type[ModelType]

    @classmethod
    async def add_one(cls, **kwargs) -> None:
        async with session() as sess:
            try:
                query = insert(cls.model).values(kwargs)
                await sess.execute(query)
                await sess.commit()
            except IntegrityError:
                await sess.rollback()

    @classmethod
    async def add_many(cls, *items) -> None:
        async with session() as sess:
            try:
                query = insert(cls.model).values(items)
                await sess.execute(query)
                await sess.commit()
            except IntegrityError:
                await sess.rollback()

    @classmethod
    async def select_filter(cls, **filter_by) -> list[ModelType]:
        async with session() as sess:
            try:
                query = select(cls.model).filter_by(**filter_by)
                result = await sess.execute(query)
                return result.scalars().all()
            except IntegrityError:
                return []

    @classmethod
    async def select_one_filter(cls, **filter_by) -> ModelType:
        async with session() as sess:
            try:
                query = select(cls.model).filter_by(**filter_by)
                result = await sess.execute(query)
                return result.scalars().first()
            except IntegrityError:
                return []

    @classmethod
    async def update_filter(cls, update_values: dict, **filter_by) -> None:
        filters = {k: v for k, v in filter_by.items() if v is not None}
        async with session() as sess:
            try:
                query = (
                    update(cls.model.__table__)
                    .filter_by(**filters)
                    .values(**update_values)
                )
                await sess.execute(query)
                await sess.commit()
            except IntegrityError:
                await sess.rollback()


class EventsDAO(BaseDAO[Events]):
    model = Events
