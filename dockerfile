# Python Image
FROM python:3.12-slim

# Setting work directory in container
WORKDIR /app

# Copy dependency list and install 
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py

# Expose the API port
EXPOSE 8000

# Start the application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
