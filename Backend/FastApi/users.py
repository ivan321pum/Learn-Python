from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Entidad user
class User(BaseModel):  # es necesario poner el BaseModel en FastAPI para no tener que poner un constructor y que
    # verifique que los tipos de datos coinciden con el introducido
    id: int
    name: str
    surname: str
    age: int


users_lists = [User(id=1, name="Iván", surname="Sevilla", age=16),
               User(id=2, name="Pepe", surname="El de los palotes", age=56),
               User(id=3, name="Paroco", surname="El del culo loco", age=156)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Iván", "surname": "Sevilla", "age": 16},
            {"name": "Pepe", "surname": "El de los palotes", "age": 56},
            {"name": "Antonio", "surname": "Ampuero", "age": 16},
            {"name": "Paroco", "surname": "Díaz", "age": 156}
            ]


@app.get("/user/{id}") #Path
async def userclass(id: int):
    if id == 0:  # Este condicional lo que hace es que si introduces 0 como parametro te devuelva todos los usuarios
        return users_lists
    else:
        users = list(filter(lambda users: users.id == id, users_lists))
        if users:
            return users
        else:
            return {"Error": "No se encontró ningún usuario con el id dado"}


@app.get("/user") #Query
async def userquery(id: Optional[int] = None):
    return search_user(id)

@app.post("/user")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        users_lists.append(user)
    else:
        return {"Error": "El usuario ya existe"}


def search_user(id: int):
    if id is None:
        return users_lists
    else:
        users = list(filter(lambda users: users.id == id, users_lists))
        try:
            return list(users)[0]
        except:
            return {"Error": "No se encontró ningún usuario con el id dado"}


#@app.delete("/user")
#async def delete_user(id:int):
