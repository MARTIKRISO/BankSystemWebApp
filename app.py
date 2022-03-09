from flask import Flask, appcontext_popped, flash, render_template, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
import pyodbc

ConnectionString = "Server=localhost/SQLEXPRESS;Database=BankSystemWebAppDB;Trusted_Connection=True;" #Connection string for DB

#Creating Database connection
cursor = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=BankSystemWebAppDB;'
                      'Trusted_Connection=yes;', 
                      autocommit= True).cursor()


app = Flask(__name__)

@app.route("/")
def index():
   pass

@app.route("/register")
def index():
   pass

@app.route("/login")
def index():
   pass

@app.route("/addfunds")
def index():
   pass

@app.route("/transerfunds")
def index():
   pass

@app.route("/changepassword")
def index():
   pass



app.run()

#HTML Templates go in templates folder, CSS and JS go in static