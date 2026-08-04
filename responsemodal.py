from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

@app.get("/users", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "password": "secret"  # This field will not be included in the response
    }

# Status code 

@app.post("create_user", response_model=UserResponse, status_code= status.HTTP_201_CREATED)
def create_user(user: User):
    return user

@app.get("/user")
def get_user():
    return {
        "status": "success",
        "message": "User retrieved successfully",
        "code": 200,
        "data": {
            "id": 1,
            "name": "John Doe",
            "age": 30
        }
    }

@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "status": "success",
        "message": "User retrieved successfully",
        "id": user_id
    }