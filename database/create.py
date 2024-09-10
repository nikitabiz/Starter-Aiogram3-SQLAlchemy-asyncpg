from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from database.dsn import get_dsn


engine = create_async_engine(
    url=get_dsn(), 
    echo=False
)

sessionmaker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase): 
    pass


class SessionManager:
    def __init__(self):
        self.sessionmaker = sessionmaker

    async def __aenter__(self):
        self.session = self.sessionmaker()
        return self.session

    async def __aexit__(self, exc_type, *args):
        if exc_type is None:
            await self.session.commit()
        else:
            await self.session.rollback()
        await self.session.close()

