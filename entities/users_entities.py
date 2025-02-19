from typing import List, Optional 
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from enum import Enum 
from config import *

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]
    email: EmailStr