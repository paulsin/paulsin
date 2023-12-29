from flask import Flask
import Nse

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World paulsin! ghgf hjhgjh fdgdfg'

@app.route('/about')
def about():
    return 'About'
