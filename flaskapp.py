from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')  # Send back to form if accessed via browser URL

    try:
        hours_input = request.form['hours']
        print(f"User input: {hours_input}")
        hours = float(hours_input)
        prediction = model.predict([[hours]])
        return render_template('results.html', prediction=round(prediction[0], 2))
    except Exception as e:
        print(f"Error: {e}")
        return "Invalid input. Please enter a valid number."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
