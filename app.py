from flask import Flask, appcontext_popped, flash, render_template, url_for, request
import DBService


#dbcontext = Service()
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
   if request.method == "GET":
      return render_template("login.html")
   else:
      #Request is POST, do the db stuff
      pass #for now

@app.route("/register", methods = ["GET", "POST"])
def register():
   if request.method == "GET":
      return render_template("register.html")
   else:
      #Request is POST, do the db stuff
      pass # for now

@app.route("/addfunds")
def addfunds():
   pass

@app.route("/transerfunds")
def transferfunds():
   pass

@app.route("/reset")
def reset():
   pass



app.run()

#HTML Templates go in templates folder, CSS and JS go in static