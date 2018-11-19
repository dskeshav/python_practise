import numpy as np
import sklearn
import pickle
from flask import Flask,request,jsonify

def predict_output():
    output={'output_pred_for_banknote':1}
    x_input=np.array([varience,skwness,curtosis,entropy])
    file='bank_note.pkl'
    M1=pickle.load(open(file,'rb'))
    return 'Hello Predictor'

app=Flask(__name__)
# @app.route('/hello', methods=['POST'])
# def index():
#     #grabs the data tagged as 'name'
#     name = request.get_json()['name']
    
#     #sending a hello back to the requester
#     return "Hello " + name
@app.route('/')
def index():
    return "Bank note authentic prediction!"


# @app.route('/predict', methods=['POST'])
# def predict():
#     #grabbing a set of wine features from the request's body
#     feature_array = request.get_json()['feature_array']
    
#     #our model rates the wine based on the input array
#     prediction = model.predict([feature_array]).tolist()
    
#     #preparing a response object and storing the model's predictions
#     response = {}
#     response['predictions'] = prediction
    
#     #sending our response object back as json
#     return jsonify(response)

@app.route('/bank_note_authentication',methods=['GET'])
def note_predict():
    body=request.get_data()
    header=request.headers
    res=predict_output()
    
    return jsonify(res)



if __name__=="__main__":
    app.run(debug=True,port=8791)
    #getting our trained model from a file we created earlier
    model = pickle.load(open("bank_note.pkl","r"))