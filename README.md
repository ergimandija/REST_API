# Recipe Platform API

This API is built using FastAPI and SQLAlchemy, providing endpoints to manage recipes and ingredients in a relational database.
![ER_Diagramm](https://github.com/user-attachments/assets/007d711b-8f9d-4704-93a9-2fe209879da4)

## Features

- **Create, Read, Update, Delete (CRUD) Operations**
  - Manage recipes and ingredients through dedicated endpoints.
- **Database Integration**
  - Utilizes SQLAlchemy for ORM and database operations.
- **RESTful Endpoints**
  - Implements CRUD operations for recipes and ingredients.
  
### Prerequisites

- Python 3.7+
- MySQL database (or compatible with SQLAlchemy)

| Datum      | Uhrzeit von - Uhrzeit bis |  Dauer in Minuten | Name  | Arbeitbeschreibung  |
|--------------|----------|-----------|---------|---------|
| 1.4.2025 | 2:00 - 2:14 | 14 | Ergi | Github-Einrichtung |
| 1.4.2025 | 2:10 - 2:24 | 14 | Rei  |Python Fast Api Project Erstellung |
| 1.4.2025 | 2:30 - 2:50 | 20 | Ergi  |MySQL-DB und Tabellen Erstellung |
| 1.4.2025 | 2:14 - 2:59 | 45 | Rei  |Verbindung mit der Datenbank |
| 1.4.2025 | 2:59 - 3:08 | 45 | Rei  |Post: /recipies/ programmieren |
| 1.4.2025 | 3:08 - 3:11 | 45 | Rei  |Postman verwenden |
| 7.4.2025 | 9:50 - 10:15 | 25 |Ergi  |MySQL Tabellen neu erstellen |
| 8.4.2025 | 14:00 - 14:13 | 13 |Rei  |Fast Api Models neu erstellen |
| 8.4.2025 | 14:00 - 14:30 | 30 |Ergi  |Post von Ingredients Programmieren |
| 8.4.2025 | 14:13 - 14:29 | 16 |Rei  |Fast Api Recipes Insert Funktion |
| 8.4.2025 | 14:30 - 15:15 | 40 |Rei  |Gets von Recipes Programmieren |
| 8.4.2025 | 14:40 - 15:20 | 40 |Ergi  |Gets von Ingredients Programmieren |
| 14.4.2025 | 9:40 - 10:20 | 40 |Ergi  |Postman Tests erstellen|
| 15.4.2025 | 13:45 - 14:30 | 40 |Ergi  |Bugfixing damit Postman Tests Funktionieren|
| 15.4.2025 | 13:45 - 14:30 | 40 |Rei  |Bugfixing damit Postman Tests Funktionieren|



# Endpoints

## Recipes

- **POST** `/recipes/`  
  Create a new recipe.
![image](https://github.com/user-attachments/assets/02a6be2c-d647-47d1-aa89-7440f3417fc1)


- **GET** `/recipes/`  
  Retrieve all recipes.
![image](https://github.com/user-attachments/assets/25f8e995-0d62-406e-91a2-e937235ac25c)

- **GET** `/recipes/{recipe_id}`  
  Retrieve a specific recipe by ID.
![image](https://github.com/user-attachments/assets/2cd2b4db-7c60-4ce3-92e6-d8e8c720fa63)


## Ingredients

- **POST** `/ingredients/`  
  Create a new ingredient.
![image](https://github.com/user-attachments/assets/20332e90-d63f-4de0-aa30-0d4993b7b6bf)

- **GET** `/ingredients/`  
  Retrieve all ingredients.
![image](https://github.com/user-attachments/assets/4a5f5bd8-3a55-4669-8dfb-ff723b18b3cd)

- **GET** `/ingredients/{ingredient_id}`  
  Retrieve a specific ingredient by ID.
![image](https://github.com/user-attachments/assets/1fad085e-41da-42aa-8646-c47f4e85dc94)

