#  Score Predictor Web App

A simple machine learning Flask app that predicts student exam scores based on hours studied.  
Deployed on Google Cloud and containerized using Docker.

---

##  Features

- Accepts study hours input via web form
- Predicts score using a trained Linear Regression model
- Clean Flask backend with HTML frontend
- Fully Dockerized and runs on port 5000
- Deployed on Google Cloud VM

---

##  How It Works

1. User enters the number of hours studied.
2. Flask sends the input to a trained model (`model.pkl`).
3. Model returns a predicted score.
4. The result is displayed on a web page.

---

##  Project Structure


