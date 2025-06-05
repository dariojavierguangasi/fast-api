from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.task_repository import ITaskRepository
from sqlalchemy.future import select

from app.models.task import Task

class TaskRepositoryImpl(ITaskRepository):

    async def get_task_by_id(self, db: AsyncSession, task_id: int) -> Task | None:
        """Get a task by its ID."""
        result = await db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()

    async def create_task(self, db: AsyncSession, task: Task) -> Task:
        """Create a new task."""
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    async def update_task(self, db: AsyncSession, task: Task) -> Task:
        """Update an existing task."""
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    async def delete_task(self, db: AsyncSession, task: Task) -> None:
        """Delete a task."""
        await db.delete(task)
        await db.commit()

    async def get_all_tasks(self, db: AsyncSession) -> list[Task]:
        """Get all tasks."""
        result = await db.execute(select(Task))
        return result.scalars().all()

    async def get_taks_by_user_id(self, db: AsyncSession, user_id: int) -> list['Task']:
        result = await db.execute(select(Task).where(Task.user_id == user_id))
        return result.scalars().all()