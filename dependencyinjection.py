from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# def common_logic():
#     # This function can contain any common logic you want to apply to multiple endpoints
#     return {"message": "This is a common logic response"}


# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data


def get_current_user():
    # This function can contain logic to retrieve the current user
    return {"user": "John Doe"}


@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return {"message": f"Welcome to the dashboard, {user['user']}!"}







def verify_token(x_token: str = Header(None)):
    if x_token != "mysecrettoken":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return {"x_token": x_token, "message": "Token is valid"}


@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {"message": "This is secure data", "user": user}


