from datetime import datetime
from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: int | None
    name: str
    email: EmailStr
    password: str
    is_active: bool
    created: datetime
    updated: datetime


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v
