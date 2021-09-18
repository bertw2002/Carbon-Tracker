from flask import Flask
from flask import render_template, request, session, redirect, url_for
import os
from utl.dbFunction import createDB, addUser, checkUsername, checkUser

app = Flask(__name__)
createDB()

@app.route("/", methods=["POST","GET"])
def root():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        userValid = checkUser(username, password)
        if username == "" or password =="":
            return render_template('homepage.html')
        if userValid:
            return redirect(url_for("interactivePage", username=username))

    return render_template('homepage.html')


# removes session data for username
@app.route("/register", methods=["POST","GET"])
def createAccount():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not checkUsername(username):
            addUser(username, password)
            return redirect(url_for("root"))

    return render_template("register.html")

@app.route("/interactivepage/<username>")
def interactivePage(username):

    return render_template("interactivepage.html")


if __name__ == "__main__":
    app.run(debug=True)
