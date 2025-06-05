from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Reemplaza esta URL por la de tu configuración real
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/tasks"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


# Dependencia asíncrona
async def get_db():
    async with async_session() as session:
        yield session
