from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()


class Items(BaseModel):
    id