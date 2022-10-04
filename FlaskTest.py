from flask import Flask, redirect, request, url_for

app = Flask(__name__)

def startFlask():
    app.run()

@app.route("/")
def home():
    index = open("index.html").read()
    return index




startFlask()