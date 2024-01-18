# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY data-generator /app/data-generator

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org kafka-python

# Define environment variable
ENV NAME World

# Run script.py when the container launches
CMD ["sh", "-c", "sleep 10 && python /app/data-generator/main.py"]
