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
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    ans=age+sex
    return jsonify({'Alert':str(ans)})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
