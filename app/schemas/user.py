from pydantic import BaseModel, EmailStr, ConfigDict, validator, field_validator

from app.exceptions.exceptions import UserNotFoundException


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if value.strip() == "" or ' ' in value:
            raise UserNotFoundException("Username cannot be empty or contain spaces.")
        return value
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> EmailStr:
        if len(value) == 0 or ' ' in value:
            raise UserNotFoundException("Email cannot be empty.")
        return value

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None

    model_config = ConfigDict(from_attributes=True)

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)