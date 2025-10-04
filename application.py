from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app = application

## import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open(r'C:/Users/mohit/Documents/Machine Learning/Projects/Algerian_Forest/models/ridge.pickle', 'rb'))
standard_scaler = pickle.load(open(r'C:/Users/mohit/Documents/Machine Learning/Projects/Algerian_Forest/models/scaler.pickle', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        input_scaled = standard_scaler.transform(input_data)
        result = ridge_model.predict(input_scaled)
        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    