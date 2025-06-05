from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.exceptions import UserNotFoundException
from app.models.user import User
from app.repositories.user_repository import IUserRepository
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user_service import IUserService


class UserServiceImpl(IUserService):

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    """
    Implementation of the IUserService interface.
    This class provides methods to manage user-related operations.
    """

    async def create_user(self, db: AsyncSession, user: UserCreate) -> UserRead:
        exist_user_with_email = await self.user_repository.get_user_by_email(user.email, db)
        if exist_user_with_email:
            raise UserNotFoundException(f"User with email {user.email} already exists.")

        user = User(**user.model_dump(exclude_unset=True))
        create_user = await self.user_repository.create_user(user, db)
        return UserRead.model_validate(create_user)

    async def get_user_by_id(self, db: AsyncSession, user_id: int) -> UserRead:
        user = await self.user_repository.get_user_by_id(user_id, db)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        return UserRead.model_validate(user)

    async def delete_user(self, db: AsyncSession, user_id: int) -> None:
        user = await self.user_repository.get_user_by_id(user_id, db)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        await self.user_repository.delete_user(db, user)
        return None

    async def get_all_users(self, db: AsyncSession) -> list[UserRead]:
        users = await self.user_repository.get_all_users(db)
        return [UserRead.model_validate(user) for user in users]

    async def update_user(self, db: AsyncSession, user_id: int, user_data: UserUpdate) -> UserRead:
        user = await self.user_repository.get_user_by_id(user_id, db)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        user = await self.user_repository.update_user(db, user)
        return UserRead.model_validate(user)
