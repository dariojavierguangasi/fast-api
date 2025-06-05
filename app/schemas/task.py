from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from datetime import datetime

from app.exceptions.exceptions import TaskNotFoundException

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not value.strip():
            raise TaskNotFoundException("Title cannot be empty.")
        return value


class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
