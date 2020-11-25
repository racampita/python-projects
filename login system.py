import json
#login system
def login():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	#check if username is in database
	jsonFile = open("users.json", "r")
	userslogin = json.load(jsonFile)
	if un in userslogin:
		if pw == userslogin[un]:
			print("Welcome")
		else:
			print("password is incorrect")
	else:
		print("username not recognized")
#signup system
def signup():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	jsonFile = open("users.json", "r")
	users = json.load(jsonFile)
	users[un] = pw
	jsonFile = open("users.json", "w")
	json.dump(users,jsonFile)
	print("You are registered")
	login()
#login or sign up
com = input("Login(1) or Signup(2): ")
if com == "1":
	login()
elif com == "2":
	signup()
else:
	print("Invalid input")
	esc = input("Press Enter to continue... ")