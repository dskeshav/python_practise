import numpy as np
import sklearn
import pickle
from flask import Flask,request,jsonify

def predict_output(varience,skwness,curtosis,entropy):
    output={'output_pred_for_banknote':1}
    x_input=np.array([varience,skwness,curtosis,entropy]).reshape(1, -1)
    file='bank_note.pkl'
    M1=pickle.load(open(file,'rb'))
    output['output_pred_for_banknote']=M1.predict(x_input)[0]
    print(output)
    return output

app=Flask(__name__)

@app.route('/')
def index():
    return "Bank note authentic prediction!"

@app.route('/bank_note_authentication',methods=['GET'])
def note_predict():
    body=request.get_data()
    header=request.headers
    
    varience,skwness,curtosis,entropy=-0.9854,-6.661,5.8245,0.5461
    try:
        res=predict_output(varience,skwness,curtosis,entropy)
    except:
        res={'failure':'exception in the prediction method'}
    return jsonify(res)


if __name__=="__main__":
    app.run(debug=True,port=8791)
    #getting our trained model from a file we created earlier
    model = pickle.load(open("bank_note.pkl","r"))