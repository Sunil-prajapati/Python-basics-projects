from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/add")
def add(a:int, b:int):
    return {"result": a + b}