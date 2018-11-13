import numpy
import sklearn
import pickle
from flask import Flask,request,jsonify

app=Flask(__name__)
@app.route('/')
def index():
    return "Bank note authentic prediction!"

@app.route('/bank_note_authentication',method=['GET'])
def note_predict():
    body=request.get_data()
    header=request.headers

    res=predict_output()




predict_output
if __name__=="__main__":
    app.run(debug=True,port=8791)