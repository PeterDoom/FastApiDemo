from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome_page():
    return "Hello World"
