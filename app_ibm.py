from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# --- WRITE THE LOADING CODE HERE ---
# This loads your model into memory once when the app starts
with open('payments.pkl', 'rb') as file:
    model = pickle.load(file)
# -----------------------------------

@app.route('/')
def home():
    return render_template('home.html')

# This is what you were missing !
if __name__ =="__main__":
    app.run(debug=True)
