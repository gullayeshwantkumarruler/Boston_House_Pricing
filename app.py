import pickle
from flask import Flask, request, jsonify, app, url_for, render_template
import pandas as pd
import numpy as np

app=Flask(__name__)  # starting point of application
regmodel=pickle.load(open('regmodel.pkl','rb'))  # loading the model
scaler=pickle.load(open('scaler.pkl','rb'))  # loading the standardscaler

@app.route('/')  # home page
def homepage():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])  # prediction page
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    prediction=regmodel.predict(new_data)
    print(prediction[0])   # as output is like a 2 d array so indexing 0
    return jsonify({'prediction':prediction[0]})

if __name__=='__main__':
    app.run(debug=True)
    