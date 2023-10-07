import os
import zlib
import json
import requests
import urllib.parse

import redis
import httpx

from fastapi import FastAPI, File, Depends, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from typing import Annotated

app = FastAPI(title="Web Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
MODEL_SERVER_URL = os.environ.get("MODEL_SERVER_URL", "http://localhost:8000")

@app.on_event("startup")
async def initialize():
    global redis_pool
    print(f"creating redis connection with {REDIS_HOST=} {REDIS_PORT=}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True
    )

def get_redis():
    return redis.Redis(connection_pool=redis_pool)

async def check_cached(text: str):
    hash = zlib.adler32(text.encode('utf-8'))
    cache = get_redis()

    data = cache.get(hash)

    return json.loads(data) if data else None

@app.post("/gpt2-infer")
async def classify_imagenet(text_input: str = Form(None)):
    infer_cache = await check_cached(text_input)

    if infer_cache == None:
        async with httpx.AsyncClient() as client:
            try:
                # print("this")
                # response = await client.post(
                #     f"{MODEL_SERVER_URL}/infer", files={"text_input": text_input}
                # )

                # print(f"response", response)

                # return response.json()
                url = f"{MODEL_SERVER_URL}/infer"
                text_input = urllib.parse.quote_plus(text_input)
                payload = f'text_input={text_input}'
                headers = {'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                }
                
                response = requests.request("POST", url, headers=headers, data=payload)

                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

                return response.json()
            except Exception as e:
                print(f"ERROR :: {e}")
                raise HTTPException(status_code=500, detail="Error from Model Endpoint")
    print("Getting data from redis cache")
    return infer_cache

# uvicorn server:app --host 0.0.0.0 --port 9000 --reload