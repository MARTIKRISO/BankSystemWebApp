import pyodbc
from werkzeug.security import generate_password_hash, check_password_hash

ConnectionString = "Server=localhost/SQLEXPRESS;Database=BankSystemWebAppDB;Trusted_Connection=True;" #Connection string for DB

class Service:
    cursor: pyodbc.Cursor
    def __init__(self):
        obj = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=BankSystemWebAppDB;'
                      'Trusted_Connection=yes;', 
                      autocommit=True).cursor()
        self.cursor = obj

    def __del__(self):
        self.cursor.close()

    def CreateUser(self, **kwargs):
        args = ""
        values = ""
        fname = kwargs.get("fname")
        mname = kwargs.get("mname", None)
        lname = kwargs.get("lname")
        SSN = kwargs.get("ssn")
        pwd = generate_password_hash(kwargs.get("pass"))
        if mname is not None:
            args = "(FirstName, MiddleName, LastName, SSN, Pwd)"
            values = f"({fname}, {mname}, {lname}, {SSN}, {pwd})"
        else:
            args = "(FirstName, LastName, SSN, Pwd)"
            values = f"({fname}, {mname}, {lname}, {SSN}, {pwd})"
        
        self.cursor.execute(f"INSERT BankSystemWebApp.Users {args} VALUES {values}")
        self.cursor.commit()
    
    def FindUser(self, **kwargs):
        
        SSN = kwargs.get("ssn")
        userpassword = kwargs.get("pass")
        
        self.cursor.execute(f"SELECT * FROM BankSystemWebApp.Users WHERE SSN = {SSN}")
        user = self.cursor.fetchone()

        #TODO: Finish this
        


