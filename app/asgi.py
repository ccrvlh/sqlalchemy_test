from fastapi import APIRouter, FastAPI
from sqlalchemy import select

from app.data import system_accounts
from app.engine import async_session, create_all, drop_all
from app.models import Tenant, User

api = FastAPI()


async def insert_all():
    users = [
        User(name="Walter"),
        User(name="Eric"),
        User(name="John"),
        Tenant(name="TenantA"),
        Tenant(name="TenantB")
    ]
    # There's an inconsistent behavior on the imported tables insert
    # Sometimes the "System Accounts" are not inserted.
    # It may be related to the cache?
    # It always works when restarting the application manually (not relying on the server's reload)
    users.extend(system_accounts)
    async with async_session() as session:
        session.add_all(users)
        await session.commit()


async def insert_all_local():
    users = [
        User(name="Walter"),
        User(name="Eric"),
        User(name="John"),
        Tenant(name="TenantA"),
        Tenant(name="TenantB")
    ]
    # This always works as the tables are "Local"
    async with async_session() as session:
        session.add_all(users)
        await session.commit()


async def get_all():
    async with async_session() as session:
        query = select(User)
        results = await session.execute(query)
    return results.scalars().all()


@api.delete("/db")
async def drop_route():
    await drop_all()
    return {"status": True, "details": "Database droppped."}

@api.post("/db")
async def create():
    await create_all()
    return {"status": True, "details": "Database created."}

@api.get("/data")
async def create():
    async with async_session() as session:
        query = select(User)
        result = await session.execute(query)
    all_users = result.scalars().all()
    response = [user.as_dict() for user in all_users]
    return response

@api.post("/data")
async def create():
    await insert_all()
    return {"status": True}

@api.post("/locals")
async def create():
    await drop_all()
    await create_all()
    await insert_all_local()
    return {"status": True}
