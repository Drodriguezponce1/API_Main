from typing import List
from fastapi import FastAPI, HTTPException

from models import User
app = FastAPI()
ID = 0
users: List[User] = [
    User(id=ID, name="John", age=25)
]

ID += 1

def updateValue():
    global ID
    ID += 1

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/users/")
def find_user():
    return users

@app.post("/users/")
def add_user(user: User):
    user.updateID(ID)
    users.append(user)
    updateValue()
    return user.id

@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user.getId() == user_id:
            return {"id": user.id, "name": user.name, "age": user.age, "email": user.email}
        
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")

