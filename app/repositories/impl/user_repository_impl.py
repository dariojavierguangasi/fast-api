from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.repositories.user_repository import IUserRepository
from app.models.user import User

class UserRepositoryImpl(IUserRepository):

    async def get_user_by_id(self, user_id: int, db: AsyncSession) -> User | None:
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_user_by_email(self, email: str, db: AsyncSession) -> User | None:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def create_user(self, user_data: User, db: AsyncSession) -> User:
        db.add(user_data)
        await db.commit()
        await db.refresh(user_data)
        return user_data

    async def update_user(self, db: AsyncSession, user_data: User) -> User:
        db.add(user_data)
        await db.commit()
        await db.refresh(user_data)
        return user_data

    async def delete_user(self, db: AsyncSession, user: User) -> None:
        await db.delete(user)
        await db.commit()

    async def get_all_users(self, db: AsyncSession) -> list[User]:
        result = await db.execute(select(User))
        return result.scalars().all()