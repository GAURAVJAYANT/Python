print("$$$ Welcome to login panel $$$")

correct_username = "gaurav"
correct_password = "test"

username = input("Enter username here:- ")
password = input("Enter password here:- ")

if username == correct_username and password == correct_password:
    print("Welcome to the system")
else:
    print("Invalid username or password")