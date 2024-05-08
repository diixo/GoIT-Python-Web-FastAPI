
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}

#uvicorn main:app --host localhost --port 8000 --reload
