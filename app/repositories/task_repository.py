from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    async def get_task_by_id(self, db: AsyncSession, task_id: int) -> 'Task | None':
        pass

    @abstractmethod
    async def create_task(self, db: AsyncSession, task: Task) -> 'Task':
        pass

    @abstractmethod
    async def update_task(self, db: AsyncSession, task: Task) -> 'Task':
        pass

    @abstractmethod
    async def delete_task(self, db: AsyncSession, task: Task) -> None:
        pass

    @abstractmethod
    async def get_all_tasks(self, db: AsyncSession) -> list['Task']:
        pass

    @abstractmethod
    async def get_taks_by_user_id(self, db: AsyncSession, user_id: int) -> list['Task']:
        pass
