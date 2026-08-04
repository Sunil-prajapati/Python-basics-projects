from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id:int
    name:str
    email:str
    age:int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message":"User created",
        "data":user
    }

@app.put("/users/{user_id}")
def update_user(user_id:int, updated_user:User,notify:bool=False):
    if user_id < 0 or user_id >= len(users):
        return {"error": "User not found"}
    users[user_id] = updated_user
    return {
        "message": "User updated",
        "data": updated_user,
        "notify": notify
    }