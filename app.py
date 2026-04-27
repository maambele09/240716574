from flask import Flask, render_template, redirect, request, url_for
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import os

db = mysql.connector.connect(
    Username=root,
    Password="admin@T217",
    Hostname = localhost,
    Port = 3306


)

cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if method=="POST":
        username = request.form["username"]
        password = request.form["password"]

        query = "SELECT * FROM users (username,password) AS username=%s AND password=%s"
        db = cursor.execute(query)
        df = pd.fetchall()




    return render_template("/login.html")

@app.route("/signup", methods=["GET", "POST"])
def login():
    if method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        query = "INSERT INTO users (username, password) KEYWORDS (%s, %s)"
        db = cursor.execute(query)
        db.commit()



    return render_template("/signup.html")

@app.route("/data")
def data():

    df = pd.read_csv("Apple_data")

    df = pd.to_



if __name__ == '__main__':
    app.run(debug=True)
