from fastapi import FastAPI

app = FastAPI()

# In-memory storage
tasks = [
    {"id": 1, "title": "Learn FastAPI", "status": "PENDING"},
    {"id": 2, "title": "Learn HTTP", "status": "COMPLETED"},
    {"id": 3, "title": "Learn API Design", "status": "INCOMPLETE"}
]


@app.get("/")
def home():
    return {"message": "Task Management API is running"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/health")
def get_health():
    return {"status": "healthy"}


@app.get("/tasks/count")
def get_count():
    return {"total": len(tasks)}