from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import os
import sqlite3


app = Flask(__name__)

@app.route("/")
def root():
    return render_template('homepage.html')

# has logout button to log out
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


# login page with form which sends request to /auth route
@app.route("/login")
def login():
    return render_template("login.html")


# removes session data for username
@app.route("/createAccount")
def createAccount():
    return render_template("createAccount.html")


if __name__ == "__main__":
    app.run(debug=True)
