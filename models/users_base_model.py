from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

database: List[User] = [
    User(
        id = uuid4(),
        first_name = "Linus",
        last_name = "Torvalds",
        gender = Gender.male,
        roles = [Role.user],
    )
]