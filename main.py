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



@app.post("/recipes/", response_model=RecipeOut)
async def create_recipe(recipe: RecipeCreate):
    query = recipes_table.insert().values(
        name=recipe.name,
        description=recipe.description,
        steps=recipe.steps
    )
    recipe_id = await database.execute(query)

    for ingredient_id in recipe.ingredients:
        await database.execute(
            recipe_ingredients_table.insert().values(
                recipe_id=recipe_id,
                ingredient_id=ingredient_id
            )
        )
    ingredients_query = sqlalchemy.select([
        ingredients_table
    ]).select_from(
        ingredients_table.join(recipe_ingredients_table,
                               ingredients_table.c.id == recipe_ingredients_table.c.ingredient_id)
    ).where(recipe_ingredients_table.c.recipe_id == recipe_id)

    ingredients = await database.fetch_all(ingredients_query)

    return {
        "id": recipe_id,
        "name": recipe.name,
        "description": recipe.description,
        "steps": recipe.steps,
        "ingredients": ingredients
    }


@app.get("/recipes/", response_model=List[RecipeOut])
async def get_recipes():
    recipes_query = recipes_table.select()
    recipes = await database.fetch_all(recipes_query)
    result = []

    for recipe in recipes:
        ingredients_query = sqlalchemy.select([
            ingredients_table
        ]).select_from(
            ingredients_table.join(recipe_ingredients_table,
                                   ingredients_table.c.id == recipe_ingredients_table.c.ingredient_id)
        ).where(recipe_ingredients_table.c.recipe_id == recipe["id"])

        ingredients = await database.fetch_all(ingredients_query)

        result.append({
            **recipe,
            "ingredients": ingredients
        })

    return result

@app.get("/recipes/{recipe_id}", response_model=RecipeOut)
async def get_recipe(recipe_id: int):
    query = recipes_table.select().where(recipes_table.c.id == recipe_id)
    recipe = await database.fetch_one(query)

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    ingredients_query = sqlalchemy.select([
        ingredients_table
    ]).select_from(
        ingredients_table.join(recipe_ingredients_table,
                               ingredients_table.c.id == recipe_ingredients_table.c.ingredient_id)
    ).where(recipe_ingredients_table.c.recipe_id == recipe_id)

    ingredients = await database.fetch_all(ingredients_query)

    return {
        **recipe,
        "ingredients": ingredients
    }


@app.post("/ingredients/", response_model=IngredientOut)
async def create_ingredient(ingredient: IngredientCreate):
    query = ingredients_table.insert().values(name=ingredient.name, type=ingredient.type)
    ingredient_id = await database.execute(query)
    return {**ingredient.dict(), "id": ingredient_id}

