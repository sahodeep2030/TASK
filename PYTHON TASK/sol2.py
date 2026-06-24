username = "admin"
password = "admin"

u=input("Enter username: ")
p=input("Enter password: ")

if u==username and p==password:
    print("Login Successful")
else:
    print("Invalid Username or Password")