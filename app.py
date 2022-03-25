from flask import Flask, flash, make_response, render_template, url_for, request, redirect
import DBService


dbcontext = DBService.DBService()
app = Flask(__name__)

@app.route("/")
@app.route("/index")
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
      status = dbcontext.CreateUser(fname=FNAME, mname=MNAME, lname=LNAME, ssn=SSN, pwd = PWD)

      return render_template("Result.html", message = status, flag = 1)
@app.route("/createaccount", methods = ["GET", "POST"])
def createaccount():
   if request.method == "GET":
      return render_template("CreateAcc.html")
   else:
      ACCNAME = request.form.get("accname")
      BAL = request.form.get("bal")
      ID = request.cookies.get('accid')
      status = dbcontext.CreateAccount(ID, bal=BAL, accname=ACCNAME)
      return render_template("Result.html", message = status)

@app.route("/addfunds", methods = ["GET", "POST"])
def addfunds():
   if request.method == "GET":
      return render_template("AddFunds.html")
   else:
      NAMEORID = request.form.get("nameid")
      VALUE = request.form.get("value")
      status = dbcontext.ChangeBalance(NAMEORID, VALUE, request.cookies.get('accid'))

   return render_template("Result.html", message = status)
   

@app.route("/transferfunds", methods = ["GET", "POST"])
def transferfunds():
   if request.method == "GET":
      return render_template("TransferFunds.html")
   else:
      SOURCENAMEORID = request.form.get("source")
      DESTINATIONNAMEORID = request.form.get("dest")
      VALUE = request.form.get("money")
      status = dbcontext.TransferFunds(request.cookies.get('accid'), source = SOURCENAMEORID, dest = DESTINATIONNAMEORID, value=VALUE)

      return render_template("Result.html", message = status)

@app.route("/user")
def user():
   id = request.cookies.get('accid')
   user = dbcontext.LookupUser(id)
   return render_template("User.html", fname = user[0], lname = user[2])


@app.route("/accounts")
def accounts():
   id = request.cookies.get('accid')
   data = dbcontext.ListAccounts(id)
   headings = ("Account Name", "Account ID", "Funds")
   return render_template("accounts.html", headings = headings, data = data)


app.run()

#HTML Templates go in templates folder, CSS and JS go in static