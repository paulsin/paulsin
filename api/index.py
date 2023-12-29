from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World paulsin! ghgfh'

@app.route('/about')
def about():
    return 'About'
