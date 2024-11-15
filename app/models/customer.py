from sqlmodel import SQLModel, Field
from typing import Optional


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    birth: str
