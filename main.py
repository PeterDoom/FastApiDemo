import datetime
import http
import random
import uuid

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/info/generate/id")
async def generate_id():
    rand_int = random.Random().randint(0, 10000)

    if rand_int >= 5121:
        return {"dateOfExecution": datetime.datetime.utcnow(), "id": uuid.uuid4()}
    elif rand_int <= 5121:
        raise HTTPException(status_code=500, detail="connection failed")
