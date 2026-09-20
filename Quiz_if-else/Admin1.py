print("welcome to groupbayport")
username="gaurav"
password="test"
username =input("Enter username here:-")
password =input("Enter password here:-")
if(username=="gaurav" and password=="test"):
    print("Login successfully")
elif(username=="gaurav"):
    if(password!="test"):
        print("username is correct but password is incorrect")
elif(username!="gaurav"):
    if(password=="test"):
        print("username is incorrect")
    else:
        print("Both username and password incorrect")
