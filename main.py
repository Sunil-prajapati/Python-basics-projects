from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()



class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    email:EmailStr
    address: Address

@app.get("/")
def home():
    return {"message": "hello world venv"}


@app.get("/about")
def about():
   return {"message":"about page"}


@app.get("/users/{user_id}")
def getUsers(user_id:int):
    return {"user id": user_id}


@app.get("/users")
def getUsers(name: str = None):
    return {"name": name}

@app.get("/products")
def getProducts(limit: int = 10):
    return {"limit": limit}


@app.get("/items")
def getProducts(name: str = None, price: int = 10):
    return {"name": name, "price": price}


@app.post("/create-user")
def createUser(user:User):
    return{
        "message":"user created",
        "data":user
    }


