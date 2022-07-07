from flask import render_template, url_for
from app import app


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return 'About'
@app.route('/<itemno>')
def item(itemno):
    return itemno
@app.route("/checkout")
def checkout():

    return render_template('checkout.html' )

@app.route("/orderConfirmation")
def orderConfirmation():

    return render_template('orderConfirmation.html' )

