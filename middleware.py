from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    print(f"Request URL: {request.url}")

    response = await call_next(request)
    print("Response Sent")
    return response

@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request processing time: {process_time:.4f} seconds")
    return response
