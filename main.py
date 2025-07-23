
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "API SF6 Buff Proxy is running!"}
