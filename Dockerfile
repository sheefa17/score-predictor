#Please see README file for instructions.
# Use a light Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt first (for faster builds if requirements don't change)
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy everything else into the container
COPY . .

# Expose the port Flask will run on (optional)
EXPOSE 5000

# Command to run the app
CMD ["python", "flaskapp.py"]
