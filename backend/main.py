from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Life Coach AI Backend is running!"}