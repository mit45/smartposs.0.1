from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    role: str = "cashier"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
