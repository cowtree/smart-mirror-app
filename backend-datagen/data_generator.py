import requests
import random
import time

while True:
    data = {"value": random.randint(1, 100)}
    response = requests.post("http://fastapi:8000/data", json=data)
    print(response.status_code, response.json())
    time.sleep(1)