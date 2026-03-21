from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.rag_chain import ask_question

app = FastAPI()

# ✅ Serve static folder properly
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Serve HTML
@app.get("/")
def home():
    return FileResponse("static/index.html")   # keep HTML in root

# Request schema
class Query(BaseModel):
    question: str

# API
@app.post("/ask")
def ask(query: Query):
    answer = ask_question(query.question)
    return {"answer": answer}