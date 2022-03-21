from curses.ascii import isnumeric
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

#=================================User Methods=========================================
    def CreateUser(self, **kwargs):
        args = ""
        values = ""
        fname = kwargs.get("fname")
        mname = kwargs.get("mname", None)
        lname = kwargs.get("lname")
        SSN = kwargs.get("ssn")
        pwd = generate_password_hash(kwargs.get("pwd"))
        if not self.UserExists(SSN):
            if mname is not None:
                args = "(FirstName, MiddleName, LastName, SSN, Pwd)"
                values = f"('{fname}', '{mname}', '{lname}', '{SSN}', '{pwd}')"
            else:
                args = "(FirstName, LastName, SSN, Pwd)"
                values = f"('{fname}', '{lname}', '{SSN}', '{pwd}')"
            
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
    
    def LookupUser(self, id):
        self.cursor.execute(f"SELECT * FROM dbo.Users WHERE id = '{id}'")
        user = self.cursor.fetchone()
        return user

    def UserExists(self, ssn):
        self.cursor.execute(f"SELECT * FROM dbo.Users WHERE SSN = '{ssn}'")

        return self.cursor.fetchone() != None
            
    def DeleteUser(self, **kwargs):
        SSN = kwargs.get("ssn")
        userpassword = kwargs.get("pwd")
        user = self.FindUser(ssn=SSN, pwd=userpassword)

        if user is not None:
            self.cursor.execute(f"DELETE FROM dbo.Users WHERE SSN='{SSN}'")
            return 0
        else:
            return -1
#=================================End User Methods=====================================
#=================================Account Methods======================================
    def ListAccounts(self, id):
        self.cursor.execute(f"SELECT dbo.BankAccounts.Name, dbo.BankAccounts.ID, dbo.BankAccounts.Balance FROM dbo.Users INNER JOIN dbo.BankAccounts ON dbo.Users.ID = dbo.BankAccounts.OwnerID WHERE OwnerID = {id};")

        field_names = [i[0] for i in self.cursor.description]
        field_names = ', '.join(field_names)
        fetched_data = self.cursor.fetchall()
        data = [tuple(rows) for rows in fetched_data]
        return tuple(data)

    def CreateAccount(self, id, **kwargs):
        name = kwargs.get("accname")
        money = kwargs.get("bal")
        ownerid = id
        values = f"('{name}', '{money}', '{ownerid}')"
        self.cursor.execute(f"INSERT dbo.BankAccounts(Name, Balance, OwnerID) VALUES {values} ")

    def ChangeBalance(self, nameorid, value):
        if isnumeric(nameorid):
            self.cursor.execute(f"UPDATE dbo.BankAccounts SET dbo.BankAccounts.Balance=dbo.BankAccounts.Balance+{value} WHERE dbo.BankAccounts.ID = '{nameorid}'")
        else:
            #got name
            pass


