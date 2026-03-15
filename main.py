from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app import ask_bot

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/ask")
def ask(q: Question):

    answer = ask_bot(q.question)

    return {"answer": answer}