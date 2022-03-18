import pyodbc
from werkzeug.security import generate_password_hash, check_password_hash

ConnectionString = "Server=localhost/SQLEXPRESS;Database=BankSystemWebAppDB;Trusted_Connection=True;" #Connection string for DB

class DBService:
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
        pwd = generate_password_hash(kwargs.get("pwd"))
        if mname is not None:
            args = "(FirstName, MiddleName, LastName, SSN, Pwd)"
            values = f"('{fname}', '{mname}', '{lname}', '{SSN}', '{pwd}')"
        else:
            args = "(FirstName, LastName, SSN, Pwd)"
            values = f"('{fname}', '{mname}', '{lname}', '{SSN}', '{pwd}')"
        
        self.cursor.execute(f"INSERT dbo.Users {args} VALUES {values}")
        self.cursor.commit()
    
    def FindUser(self, **kwargs):
        
        SSN = kwargs.get("ssn")
        userpassword = kwargs.get("pwd")
        
        self.cursor.execute(f"SELECT * FROM dbo.Users WHERE SSN = '{SSN}'")
        user = self.cursor.fetchone()
        passfromdb = user[5]
        
        if check_password_hash(passfromdb, userpassword):
            return user
        else:
            return None
            
    def DeleteUser(self, **kwargs):
        SSN = kwargs.get("ssn")
        userpassword = kwargs.get("pwd")
        user = self.FindUser(ssn=SSN, pwd=userpassword)

        if user is not None:
            self.cursor.execute(f"DELETE FROM dbo.Users WHERE SSN='{SSN}'")
            return 0
        else:
            return -1


        


