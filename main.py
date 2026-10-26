from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Management API is running"}


@app.get("/tasks")
def get_tasks():
    return [
        {
            "id": 1,
            "title": "Learn FastAPI",
            "status": "PENDING"
        },
        {
            "id": 2,
            "title": "Learn HTTP",
            "status": "COMPLETED"
        }
    ]