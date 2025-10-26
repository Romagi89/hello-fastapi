from fastapi import FastAPI
import os
import asyncpg

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world from FastAPI + Harness + EKS!-AutoTrigger-Test1"}

@app.get("/db-check")
async def db_check():
    conn = await asyncpg.connect(
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        database=os.environ["POSTGRES_DB"],
    )
    await conn.close()
    return {"status": "PostgreSQL connection successful"}
