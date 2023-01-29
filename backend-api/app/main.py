from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    value: int

app = FastAPI()

data_storage = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/data")
async def receive_data(data: Data):
    # store the data in the data_storage list
    print(data.dict())
    data_storage.append(data.dict())
    return {"message": "Data received"}

@app.get("/data")
async def get_data():
    # return the data stored in the data_storage list
    try:
        # Return the data from the in-memory store
        return {"data": data_storage}
    except Exception as e:
        logging.error(f"Error getting data: {e}")
        raise


