# 🤖 Contract PDF RAG Chatbot

A simple **AI chatbot that answers questions from contract PDFs** using **Retrieval Augmented Generation (RAG)**.

This project demonstrates how to build an **AI document assistant** using **FastAPI, LangChain, Docker, GitHub CI/CD, and AWS (EC2 + ECR)**.

---

# 🚀 Features

* 📄 Ask questions from contract PDFs
* 🤖 AI-powered chatbot responses
* 🌙 Dark mode chatbot interface with robot icon
* 🐳 Docker containerization
* ☁ Deployment on AWS EC2
* ⚙ GitHub Actions CI/CD pipeline
* 🧠 Vector search using embeddings

---

# 📂 Project Structure

```text
contract-rag-bot
│
├── app
│   ├── main.py
│   └── rag_pipeline.py
│
├── ingestion
│   └── ingest.py
│
├── templates
│   └── index.html
│
├── data
│   └── contracts
│
├── requirements.txt
├── Dockerfile
└── .github/workflows/deploy.yml
```

---

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

# 🤖 Example Questions

You can ask questions like:

* What are the payment terms?
* What is the termination clause?
* When does the contract expire?
* What is the confidentiality clause?

---

# 🐳 Docker

Build Docker image

```bash
docker build -t contract-rag-bot .
```

Run container

```bash
docker run -p 8000:8000 contract-rag-bot
```

---

# ☁ AWS Deployment

This project uses:

* AWS EC2 (to run the application)
* AWS ECR (to store Docker images)

Steps:

1. Push Docker image to ECR
2. Pull the image in EC2
3. Run the container

Application will run at:

```
http://EC2_PUBLIC_IP:8000
```

---

# ⚙ CI/CD

GitHub Actions automatically:

1. Builds Docker image
2. Pushes image to AWS ECR
3. Deploys to EC2

Workflow file:

```
.github/workflows/deploy.yml
```

---

# 🛠 Tech Stack

Backend

* Python
* FastAPI

AI

* LangChain
* OpenAI

Vector Database

* ChromaDB

Cloud

* AWS EC2
* AWS ECR

DevOps

* Docker
* GitHub Actions

Frontend

* HTML
* CSS
* JavaScript

---

# 👨‍💻 Author

Jayachandra
