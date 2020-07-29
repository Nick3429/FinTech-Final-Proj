# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/currencyexchange')
def currencyexchange():
    return render_template("currencyexchange.html", time = datetime.now())

@app.route('/flights')
def flights():
    return render_template("flights.html", time = datetime.now())