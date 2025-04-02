import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "ShadowTact v1.3 Cloud is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
