FROM python:3.8-slim

# Create working directory
WORKDIR /opt/flask_insurance

# Copy requirements and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy all project files to container
COPY . .

# Generate the model.pkl file
RUN python3.8 model.py

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python3.8", "flaskapp.py"]
 49aec41 (Update Dockerfile to build model.pkl during image build)
