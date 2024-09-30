# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt /code/requirements.txt

# Install any dependencies specified in requirements.txt
RUN pip install "fastapi[standard]"
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app
COPY ./tests /code/tests
COPY ./utils /code/utils

# Expose the port that the app runs on
EXPOSE 8080

# Command to run the FastAPI app with uvicorn
CMD ["fastapi", "run", "app/main.py","--port", "8080"]
