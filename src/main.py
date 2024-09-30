from fastapi import FastAPI
from os import environ as env
app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello, Fastapi Template Is Ready - {env['Environment']}"}