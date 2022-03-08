from flask import Flask, render_template, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
import pyodbc

ConnectionString = "Server=localhost/SQLEXPRESS;Database=BankSystemWebAppDB;Trusted_Connection=True;" #Connection string for DB

#Creating Database connection
cursor = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=BankSystemWebAppDB;'
                      'Trusted_Connection=yes;', 
                      autocommit= True).cursor()