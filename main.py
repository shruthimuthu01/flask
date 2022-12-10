from flask import Flask,request,jsonify
import os
import numpy as np
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
