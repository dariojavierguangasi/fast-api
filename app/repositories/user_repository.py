from abc import ABC,abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User


class IUserRepository(ABC):

    @abstractmethod
    async def get_user_by_id(self, user_id: int, db: AsyncSession) -> User | None:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str, db: AsyncSession) -> User | None:
        pass

    @abstractmethod
    async def create_user(self, user_data: User, db: AsyncSession) -> User:
        pass

    @abstractmethod
    async def update_user(self, db: AsyncSession, user_data: User) -> User:
        pass

    @abstractmethod
    async def delete_user(self, db: AsyncSession, user: User) -> None:
        pass

    @abstractmethod
    async def get_all_users(self, db: AsyncSession) -> list[User]:
        pass
