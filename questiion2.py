
def login(password,a="admin"):
    if password == "123":
        print("Login Sucessfully")
    else:
        print("Login Failed")

password = input("enter password")
login(password)