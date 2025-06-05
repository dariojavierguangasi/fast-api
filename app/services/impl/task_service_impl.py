from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.exceptions import TaskNotFoundException, UserNotFoundException
from app.models.task import Task
from app.repositories.task_repository import ITaskRepository
from app.repositories.user_repository import IUserRepository
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import ITaskService


class TaskServiceImpl(ITaskService):

    def __init__(self, task_repository: ITaskRepository, user_repository: IUserRepository):
        self.task_repository = task_repository
        self.user_repository = user_repository

    async def create_task(self, db: AsyncSession, task_data: TaskCreate) -> TaskRead:
        exist_user = await self.user_repository.get_user_by_id(task_data.user_id, db)

        if not exist_user:
            raise UserNotFoundException(f"User with ID {task_data.user_id} does not exist.")

        create_task = Task(**task_data.model_dump(exclude_unset=True))
        task = await self.task_repository.create_task(db, create_task)
        return TaskRead.model_validate(task)

    async def get_task_by_id(self, db: AsyncSession, task_id: int) -> TaskRead:
        task = await self.task_repository.get_task_by_id(db, task_id)
        if not task:
            raise TaskNotFoundException(f"Task with ID {task_id} not found.")
        return TaskRead.model_validate(task)

    async def delete_task(self, db: AsyncSession, task_id: int) -> None:
        task = await self.task_repository.get_task_by_id(db, task_id)
        if not task:
            return None
        await self.task_repository.delete_task(db, task)

    async def get_all_tasks(self, db: AsyncSession) -> list[TaskRead]:
        tasks = await self.task_repository.get_all_tasks(db)
        return [TaskRead.model_validate(task) for task in tasks] if tasks else []

    async def update_task(self, db: AsyncSession, task_id: int, task_data: TaskUpdate) -> TaskRead:
        task = await self.task_repository.get_task_by_id(db, task_id)
        if not task:
            raise TaskNotFoundException(f"Task with ID {task_id} not found.")
        for key, value in task_data.model_dump(exclude_unset=True).items():
            setattr(task, key, value)
        updated_task = await self.task_repository.update_task(db, task)
        return TaskRead.model_validate(updated_task)

    async def get_tasks_by_user_id(self, db: AsyncSession, user_id: int) -> list[TaskRead]:
        exist_user = await self.user_repository.get_user_by_id(user_id, db)
        if not exist_user:
            raise UserNotFoundException(f"User with ID {user_id} does not exist.")
        tasks = await self.task_repository.get_taks_by_user_id(db, user_id)
        return [TaskRead.model_validate(task) for task in tasks] if tasks else []
