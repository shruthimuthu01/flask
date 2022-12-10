from flask import Flask,request,jsonify
import os
import numpy as np
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return "hello1"

@app.route('/predict',methods=['POST'])
def predict():
    with open('logit_pkl', 'rb') as f:
        logit_model = pickle.load(f, encoding='UTF-8')
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    cpt = int(request.form.get('cpt'))
    bp = float(request.form.get('bp'))
    chol = float(request.form.get('chol'))
    fbs = int(request.form.get('fbs'))
    ekg = int(request.form.get('ekg'))
    hr = float(request.form.get('hr'))
    ea = int(request.form.get('ea'))
    st = float(request.form.get('st'))
    sts = int(request.form.get('sts'))
    flo = int(request.form.get('flo'))
    t = int(request.form.get('t'))
    lis=[[age,sex,cpt,bp,chol,fbs,ekg,hr,ea,st,sts,flo,t]]
    
    ans=age+sex
    return jsonify({'Alert':str(ans)})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
