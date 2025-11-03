import os
from typing import Optional
from fastapi import FastAPI, Query
from pymongo import MongoClient
import uvicorn

app = FastAPI()
client = MongoClient(os.environ['MONGO_URI'])
collection = client['energy']['power_consumption']

@app.get("/power_consumption")
def get_power_consumption(from_timestamp: Optional[int] = Query(default=None, alias='from'),
                          to_timestamp: Optional[int] = Query(default=None, alias='to')):
    query = {}
    if from_timestamp is not None:
        query['timestamp'] = {'$gte': from_timestamp}
    if to_timestamp is not None:
        query['timestamp'] = {'$lte': to_timestamp}
    data = list(collection.find(query))
    result = [
        {k: v for k, v in doc.items() if k not in {'_id'}}
        for doc in data
    ]
    return {'power_consumption': result}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)