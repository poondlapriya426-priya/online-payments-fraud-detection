import os
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Correct pathing to find the model file
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'payments.pkl')

# Load the model with an error check
model = None
if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('submit.html', prediction_text="Error: Model not loaded.")
    
    # Get values from the form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    
    result = "Fraudulent" if prediction[0] == 1 else "Normal"
    return render_template('submit.html', prediction_text=f'Transaction is {result}')

if __name__ == "__main__":
    app.run(debug=True)