# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
from model import theanswer
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

@app.route('/results', methods = ["GET","POST"])
def results():
    if request.method == 'POST':
        theprice = request.form['base']
        theunit = request.form['new']
        themoney = request.form['money']
        answer = theanswer(theprice, theunit, themoney)
        return render_template("results.html", answer = answer, theunit = theunit, time = datetime.now())
    else:
        return "error"