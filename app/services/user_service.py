from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserRead, UserCreate, UserUpdate


class IUserService(ABC):

    @abstractmethod
    async def create_user(self, db: AsyncSession, user: UserCreate) -> UserRead:
        pass

    @abstractmethod
    async def get_user_by_id(self, db: AsyncSession, user_id: int) -> UserRead:
        pass

    @abstractmethod
    async def delete_user(self, db: AsyncSession, user_id: str) -> None:
        pass

    @abstractmethod
    async def get_all_users(self, db: AsyncSession) -> list[UserRead]:
        pass

    @abstractmethod
    async def update_user(self, db: AsyncSession, user_id: int, user_data: UserUpdate) -> UserRead:
        pass