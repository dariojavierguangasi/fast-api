from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.impl.task_repository_impl import TaskRepositoryImpl
from app.repositories.impl.user_repository_impl import UserRepositoryImpl
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.services.impl.task_service_impl import TaskServiceImpl

route = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

task_service = TaskServiceImpl(TaskRepositoryImpl(), UserRepositoryImpl())


@route.get("/all", response_model=list[TaskRead], status_code=status.HTTP_200_OK)
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    return await task_service.get_all_tasks(db)


@route.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_service.create_task(db, task_data)


@route.get("/{task_id}", response_model=TaskRead, status_code=status.HTTP_200_OK)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await task_service.get_task_by_id(db, task_id)


@route.put("/{task_id}", response_model=TaskRead, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task_data: TaskUpdate, db: AsyncSession = Depends(get_db)):
    return await task_service.update_task(db, task_id, task_data)


@route.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await task_service.delete_task(db, task_id)


@route.get("/user/{user_id}", response_model=list[TaskRead], status_code=status.HTTP_200_OK)
async def get_tasks_by_user_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await task_service.get_tasks_by_user_id(db, user_id)
