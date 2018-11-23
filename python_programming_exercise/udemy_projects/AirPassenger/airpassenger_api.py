import numpy as np
import pandas as pd
import sklearn
from flask import Flask,request,jsonify
import pickle
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMAResults

def predict_output():
    output={'Number of passenger': 0}
    x_input=datetime.date(datetime(1949,1,1))
    print(x_input)
    file='airpassenger.pkl'
    from pandas import Series
    from statsmodels.tsa.arima_model import ARIMAResults
    import numpy

    # invert differenced value
    def inverse_difference(history, yhat, interval=1):
        return yhat + history[-interval]

    M1=pickle.load(open(file,'rb'))
    output['Number of passenger']=M1.predict(x_input)[0]
    print(output)
    return output

app=Flask(__name__)

@app.route('/')
def index():
    return "Air passenger predict"

@app.route('/Airpassengerpredict',methods=['GET'])
def note_predict():
    body=request.get_data()
    header=request.headers

    # try:
    res=predict_output()
    # except:
    #     res={'failure':'exception in the prediction method'}
    return jsonify(res)


if __name__=="__main__":
    app.run(debug=True,port=8791)
    #getting our trained model from a file we created earlier
    model = pickle.load(open("airpassenger.pkl","r"))