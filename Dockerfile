#official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run Uvicorn with host 0.0.0.0 so it's accessible externally
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]