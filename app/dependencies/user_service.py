from app.repositories.impl.user_repository_impl import UserRepositoryImpl
from app.services.impl.user_service_impl import UserServiceImpl
from app.services.user_service import IUserService


def get_user_service() -> IUserService:
    repo = UserRepositoryImpl()
    return UserServiceImpl(repo)
