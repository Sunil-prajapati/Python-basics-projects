import requests
from fastapi import FastAPI, HTTPException


#By using Python
# response = requests.get("https://jsonplaceholder.typicode.com/posts")


# data = response.json()
# print(data )

app = FastAPI()

#GET ALL POSTS
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching posts")

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Post not found")

