from asyncio.windows_events import NULL
from os import access
from flask import Flask, appcontext_popped, flash, make_response, render_template, url_for, request, redirect
import DBService


dbcontext = DBService.DBService()
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
   if request.method == "GET":
      return render_template("login.html")
   else:
      SSN = request.form["ssn"]
      PWD = request.form["pwd"]

      loggedin = dbcontext.FindUser(ssn=SSN, pwd=PWD)
      print(loggedin)

      if loggedin is None:
         return "wrong pwd"
      else:
         resp = make_response(redirect("/user"))
         resp.set_cookie('accid', str(loggedin[4]))
         return resp
        # return redirect(url_for("user", user = loggedin))

@app.route("/register", methods = ["GET", "POST"])
def register():
   if request.method == "GET":
      return render_template("register.html")
   else:
      MNAME = None
      FNAME = request.form.get("fname")
      MNAME = request.form.get("mname")
      LNAME = request.form.get("lname")
      SSN = request.form.get("SSN")
      PWD = request.form.get("pwd")
      dbcontext.CreateUser(fname=FNAME, mname=MNAME, lname=LNAME, ssn=SSN, pwd = PWD)

      return "done"
@app.route("/createaccount", methods = ["GET", "POST"])
def createaccount():
   if request.method == "GET":
      return render_template("CreateAcc.html")
   else:
      ACCNAME = request.form.get("accname")
      BAL = request.form.get("bal")
      ID = request.cookies.get('accid')
      dbcontext.CreateAccount(ID, bal=BAL, accname=ACCNAME)

      return "done"

@app.route("/addfunds", methods = ["GET", "POST"])
def addfunds():
   if request.method == "GET":
      return render_template("AddFunds.html")
   else:
      NAMEORID = request.form.get("nameid")
      VALUE = request.form.get("value")
      dbcontext.ChangeBalance(NAMEORID, VALUE, request.cookies.get('accid'))

      return "done"
   

@app.route("/transerfunds")
def transferfunds():
   pass

@app.route("/reset")
def reset():
   pass

@app.route("/user")
def user():
   id = request.cookies.get('accid')
   user = dbcontext.LookupUser(id)
   return render_template("User.html", fname = user[0], lname = user[2])

@app.route("/delete")
def delete():
   pass

@app.route("/accounts")
def accounts():
   id = request.cookies.get('accid')
   data = dbcontext.ListAccounts(id)
   headings = ("Account Name", "Account ID", "Funds")
   return render_template("accounts.html", headings = headings, data = data)


app.run()

#HTML Templates go in templates folder, CSS and JS go in static