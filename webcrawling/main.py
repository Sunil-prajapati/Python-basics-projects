from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import requests
import time

app = FastAPI()


#Cache Storage
cache_data = []
last_fetch_time = 0

@app.get("/news")
def get_news(): 
    global cache_data, last_fetch_time
    start = time.time()
    if time.time() - last_fetch_time > 60:
        print("Fetching new data from Hacker News...")
        url = "https://news.ycombinator.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        cache_data = [
            item.text for item in soup.select(".titleline a")
        ]
        last_fetch_time = time.time()
    else:
        print("Returning cached data...")

    end = time.time()
    print(f"Execution time: {end - start} seconds")
    return cache_data
