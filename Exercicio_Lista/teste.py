from datetime import datetime
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4, UUID

app = FastAPI()

users = {}

class User(BaseModel):
    id: Optional[UUID]
    name: str
    email: str
    password: str
    date_cretated: datetime




@app.get('/users')
async def get_users():
    return users

@app.post('users')
async def create_user(user: User):
    user.id = uuid4
    users[user.id]={user}
    return user
