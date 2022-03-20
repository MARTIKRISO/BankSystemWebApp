import DBService
#Accs pwds: 123martin, spas123
serv = DBService.DBService()

#print(serv.FindUser(ssn="1234567892", pwd="hristo3123"))

#serv.CreateUser(fname="Martin", mname="Stanimirov", lname="Shkodrov", ssn="1234567891", pwd= "123martin")

#serv.DeleteUser(ssn="1234567891", pwd="123martin")
#print(serv.UserExists("1234567891"))

print(serv.ListAccounts(6))
