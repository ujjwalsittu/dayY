from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

    class Config:
        orm_mode = True
