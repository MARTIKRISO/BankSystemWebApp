import DBService
#Accs pwds: 123martin, spas123
serv = DBService.DBService()

print(serv.FindUser(ssn="1234567891", pwd="123martin"))

#serv.CreateUser(fname="Martin", mname="Stanimirov", lname="Shkodrov", ssn="1234567891", pwd= "123martin")

#serv.DeleteUser(ssn="1234567891", pwd="123martin")