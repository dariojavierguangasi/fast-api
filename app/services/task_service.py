from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.task import TaskCreate, TaskRead, TaskUpdate


class ITaskService(ABC):
    @abstractmethod
    async def create_task(self, db: AsyncSession, task_data: TaskCreate) -> TaskRead:
        pass

    @abstractmethod
    async def get_task_by_id(self, db: AsyncSession, task_id: int) -> TaskRead:
        pass

    @abstractmethod
    async def delete_task(self, db: AsyncSession, task_id: int) -> None:
        pass

    @abstractmethod
    async def get_all_tasks(self, db: AsyncSession) -> list[TaskRead]:
        pass

    @abstractmethod
    async def update_task(self, db: AsyncSession, task_id: int, task_data: TaskUpdate) -> TaskRead:
        pass

    @abstractmethod
    async def get_tasks_by_user_id(self, db: AsyncSession, user_id: int) -> list[TaskRead]:
        pass
