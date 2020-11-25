import json
#when logged in, you can delete your account
def logedin(un):
	delete = input("Do you want to delete your account? (Y/N)")
	if delete == "Y":
		
		input("Account deleted. Press Enter to continue...")


#login system
def login():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	#check if username is in database
	
	if un in userslogin:
		if pw == userslogin[un]:
			print("Welcome")
			logedin(un)
		else:
			print("password is incorrect")
	else:
		print("username not recognized")
#signup system
def signup():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")

	print("You are registered")
	login()
#login or sign up
print(open("users.json", "r"))
com = input("Login(1) or Signup(2): ")
if com == "1":
	login()
elif com == "2":
	signup()
else:
	print("Invalid input")
	esc = input("Press Enter to continue... ")