from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    role: str = "cashier"


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    # Pydantic v2: use from_attributes instead of orm_mode
    model_config = {"from_attributes": True}
