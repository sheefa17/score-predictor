
FROM python:3.8
WORKDIR /opt/flask_insurance
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python3.8 model.py
EXPOSE 5000
CMD ["python", "flaskapp.py"]
