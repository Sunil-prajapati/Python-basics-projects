import time
from fastapi import FastAPI
import asyncio

app = FastAPI()

# def task():
#     time.sleep(2)
#     print("Task 1 completed")

# async def async_task():
#     await asyncio.sleep(3)
#     print("Task 2 completed")

@app.get("/sync")
async def sync_endpoint():
    await asyncio.sleep(3) 
    return {
        "message": "This is a synchronous endpoint that simulates a long-running task.",
    }