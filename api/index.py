from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the data from JSON
with open("data.json", "r") as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(name: list[str]):
    marks = [student_marks.get(n, "Not found") for n in name]
    return {"marks": marks}
