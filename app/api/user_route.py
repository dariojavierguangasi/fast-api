from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.impl.user_repository_impl import UserRepositoryImpl
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.impl.user_service_impl import UserServiceImpl

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

user_service = UserServiceImpl(UserRepositoryImpl())


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db, user)


@router.get("/all", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await user_service.get_all_users(db)


@router.put("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_data: UserUpdate, db: AsyncSession = Depends(get_db)):
    return await user_service.update_user(db, user_id, user_data)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_service.delete_user(db, user_id)


@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_service.get_user_by_id(db, user_id)
