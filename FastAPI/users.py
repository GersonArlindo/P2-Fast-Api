from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn users:app --reload

#Definiendo entidad user 
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Gerson",  surname="Gonzalez", url="https://moure.dev", age=10),
              User(name="Amada",  surname="Calis", url="https://mouredev.com", age=20),
              User(name="Arlindo",  surname="Vasquez", url="https://moure.dev", age=30)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Gerson", "surname": "Gonzalez", "url":"https://moure.dev", "age": 10},
            {"name": "Genesis", "surname": "Gonzalez", "url":"https://moure.dev", "age": 20},
            {"name": "Helen", "surname": "Nicole", "url":"https://moure.dev", "age": 30}]

@app.get("/users")
async def users():
    return users_list