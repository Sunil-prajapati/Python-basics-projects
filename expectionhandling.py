from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class UserNotFoundException(HTTPException):
    def __init__(self, name: str):
       self.name = name


@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User '{exc.name}' not found",
            "code": 404
        }
    )

# Custom error
@app.get("/users/{name}")
def get_user_by_name(name: str):
    if name != "John Doe":
        raise UserNotFoundException(name)
    return {
        "status": "success",
        "message": "User retrieved successfully",
        "name": name
    }



@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "status": "success",
        "message": "User retrieved successfully",
        "id": user_id
    }


