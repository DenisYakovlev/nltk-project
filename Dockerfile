# Use the official latest Python image
FROM python:latest

# Set working directory inside the container
WORKDIR /app

# Copy and install requirements
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
CMD ["python3", "./src/main.py"]