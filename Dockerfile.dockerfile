# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y libmariadb-dev pkg-config gcc

# Install Flask and other dependencies
RUN pip install Flask Flask-MySQLdb Flask-CORS

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]



