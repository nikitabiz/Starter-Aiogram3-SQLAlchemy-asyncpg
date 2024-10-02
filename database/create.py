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
