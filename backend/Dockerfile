# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /backend

# Upgrade pip
RUN pip install --upgrade pip

# Install FastAPI and standard dependencies
RUN pip install "fastapi[standard]"

# Copy the requirements file and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application backend
COPY backend/ .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
