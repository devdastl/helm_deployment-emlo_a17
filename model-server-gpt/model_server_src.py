import urllib
import io
import os
import zlib
import json

import redis

import torch
import numpy as np
from transformers import GPT2Tokenizer, GPT2LMHeadModel

from fastapi import FastAPI, File, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from typing import Dict, Annotated

app = FastAPI(title="Model Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TOKENIZER = os.environ.get("TOKENIZER_MODEL", "gpt2")
GPT_MODEL = os.environ.get("GPT_MODEL", "gpt2")
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")

@app.on_event("startup")
async def initialize():
    # initializes model, tokenizer, redis connection
    global gpt_model
    print(f"loading model {GPT_MODEL=}...")
    gpt_model = GPT2LMHeadModel.from_pretrained(GPT_MODEL)
    print(f"loaded model {GPT_MODEL=}")

    global tokenizer
    print(f"loading tokenizer {TOKENIZER=}...")
    tokenizer = GPT2Tokenizer.from_pretrained(TOKENIZER)
    print(f"loaded tokenizer {TOKENIZER=}")

    # global categories
    # # Download human-readable labels for ImageNet.
    # # get the classnames
    # url, filename = (
    #     "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt",
    #     "imagenet_classes.txt",
    # )
    # urllib.request.urlretrieve(url, filename)
    # with open("imagenet_classes.txt", "r") as f:
    #     categories = [s.strip() for s in f.readlines()]

    global redis_pool
    print(f"creating redis connection with {REDIS_HOST=} {REDIS_PORT=}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True
    )

def get_redis():
    # Here, we re-use our connection pool
    # not creating a new one
    return redis.Redis(connection_pool=redis_pool)

def predict(text: str) -> str:
    encoded_input = tokenizer(text, return_tensors='pt')
    output = gpt_model.generate(**encoded_input, max_new_tokens=10)
    decoded = tokenizer.decode(output[0])
    return {"predicted_text":str(decoded)}

async def write_to_cache(text: str, result: Dict[str, str]) -> None:
    cache = get_redis()

    hash = zlib.adler32(text.encode('utf-8'))
    cache.set(hash, json.dumps(result))

@app.post("/infer")
async def infer(text_input: str = Form(None)):

    predictions = predict(text_input)

    await write_to_cache(text_input, predictions)

    return predictions

# uvicorn model_server_src:app --host 0.0.0.0 --port 8000 --reload