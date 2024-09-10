from database.create import engine, Base
from database.models import *


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)