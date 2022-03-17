import pyodbc

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

    def Create(self, **kwargs):
        args = ""
        values = ""
        fname = kwargs.get("fname")
        mname = kwargs.get("mname", None)
        lname = kwargs.get("lname")
        SSN = kwargs.get("ssn")
        pwd = kwargs.get("pass")
        
        if mname is not None:
            args = "(FirstName, MiddleName, LastName, SSN, Pwd)"
            values = f"({fname}, {mname}, {lname}, {SSN}, {pwd})"
        else:
            args = "(FirstName, LastName, SSN, Pwd)"
            values = f"({fname}, {mname}, {lname}, {SSN}, {pwd})"
        
        self.cursor.execute(f"INSERT BankSystemWebApp.Client {args} VALUES {values}")
        self.cursor.commit()

