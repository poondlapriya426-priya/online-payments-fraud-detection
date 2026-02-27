from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('payments.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the form
    input_features = [float(x) for x in request.form.values()]
    features = [np.array(input_features)]
    
    # Make prediction
    prediction = model.predict(features)
    
    # Determine the message
    if prediction[0] == 1:
        output = "Fraudulent"
    else:
        output = "Normal"
        
    return render_template('submit.html', prediction_text=f'Transaction is {output}')

if __name__ == "__main__":
    app.run ( debug=True )
