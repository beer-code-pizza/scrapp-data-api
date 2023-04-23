# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /code

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api

# Run app.py when the container launches
CMD ["python3", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]