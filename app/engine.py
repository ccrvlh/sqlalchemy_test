from logging import getLogger
from typing import Callable

import sqlalchemy as db
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import close_all_sessions, declarative_base, sessionmaker

logger = getLogger(__name__)

async_engine = create_async_engine("postgresql+asyncpg://@localhost:5432/sqltest", echo=True)
async_session: Callable[..., AsyncSession] = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()


class BaseMixin:
    __mapper_args__ = {"always_refresh": False}
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    seq = db.Column(db.Integer, db.Identity(start=1000, cycle=True))


async def create_all() -> None:
    """Create all tables"""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    return


async def drop_all() -> None:
    """Drop all tables"""
    logger.info("Dropping database...")
    close_all_sessions()
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.commit()
    logger.info("Dropped database.")
    return
