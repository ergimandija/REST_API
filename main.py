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
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(200)),
    sqlalchemy.Column("steps", sqlalchemy.String(500)),
)

ingredients_table = sqlalchemy.Table(
    "ingredients",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("type", sqlalchemy.String(50)),
)

recipe_ingredients_table = sqlalchemy.Table(
    "recipe_ingredients",
    metadata,
    sqlalchemy.Column("recipe_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("recipes.id"), primary_key=True),
    sqlalchemy.Column("ingredient_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("ingredients.id"), primary_key=True),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

class IngredientCreate(BaseModel):
    name: str
    type: str

class IngredientOut(BaseModel):
    id: int
    name: str
    type: str

class RecipeCreate(BaseModel):
    name: str
    description: str
    steps: str
    ingredients: List[int]

class RecipeOut(BaseModel):
    id: int
    name: str
    description: str
    steps: str
    ingredients: List[IngredientOut]


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
