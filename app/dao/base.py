from app.database import async_session_maker
from sqlalchemy import select, insert, desc


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def last_3_request(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).order_by(desc(cls.model.id)).filter_by(**filter_by).limit(3)
            result = await session.execute(query)
            return result.mappings().all()


