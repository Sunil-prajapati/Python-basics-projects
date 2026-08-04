from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

#Limiter configuration
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

#Error Handler
@app.exception_handler(RateLimitExceeded)
def handle_rate_limit_exceeded(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )

#Rate Limiter Api
@app.get("/limited")
@limiter.limit("5/minute")  # Limit to 5 requests per minute
def get_data(request: Request):
    return {"message": "This endpoint is rate limited."}