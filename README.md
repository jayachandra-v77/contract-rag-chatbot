## 🤖 Contract PDF RAG Chatbot

A simple **AI chatbot that answers questions from contract PDFs** using **Retrieval Augmented Generation (RAG)**.

This project demonstrates how to build an **AI document assistant** using **FastAPI, LangChain, Docker, GitHub CI/CD, and AWS (EC2 + ECR)**.

-------

###  Features

* 📄 Ask questions from contract PDFs
* 🤖 AI-powered chatbot responses
* 🌙 Dark mode chatbot interface with robot icon
* 🧠 Vector search using embeddings



# ⚙ Installation (Local)

Clone the repository

```bash
git clone https://github.com/your-username/contract-rag-bot.git
cd contract-rag-bot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open in browser

```
http://localhost:8000
```

---

### Example Questions

You can ask questions like:

* What are the payment terms?
* What is the termination clause?
* When does the contract expire?
* What is the confidentiality clause?

### Tech Stack

Backend

* Python
* FastAPI

AI

* LangChain
* OpenAI

Vector Database

* PINECONE


Frontend

* HTML
* CSS
* JavaScript

---

### Author

Jayachandra
