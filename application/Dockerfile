# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt ./app.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install opentelemetry-distro[otlp]
RUN opentelemetry-bootstrap -a install

# Make port 8082 available to the world outside this container
EXPOSE 8082

# Run app.py when the container launches
CMD ["opentelemetry-instrument", "flask", "run", "--host", "0.0.0.0", "--port", "8082"]
