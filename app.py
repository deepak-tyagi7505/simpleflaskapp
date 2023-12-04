from flask import Flask
import gunicorn
import wfastcgi

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
