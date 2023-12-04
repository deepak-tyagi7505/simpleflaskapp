from flask import Flask
    
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World This is the First applcation in flask app'

if __main__ == '__main__':
    app.run()
