from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/20wk2yc8p6caztasx7bb")
def hello_poc():
    return "<!-- PoC -->"
