import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import databases
import sqlalchemy

DATABASE_URL = os.environ.get("DATABASE_URL", "mysql+pymysql://ergimandija:!Insy_2023$@htl-projekt.com:3306/2024_4bx_ergimandija_recipeplatform")
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

recipes_table = sqlalchemy.Table(
    "recipes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

ingredients_table = sqlalchemy.Table(
    "ingredients",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

class Ingredient(BaseModel):
    name: str
    type: str
    r_id: int

class Recipe(BaseModel):
    name: str
    description: str
    steps: str
    ingredients: List[int]

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

