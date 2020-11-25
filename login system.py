import json
#when logged in, you can delete your account
def logedin(un):
	delete = input("Do you want to delete your account? (Y/N)")
	if delete == "Y" or delete == "y":
		with open("users.json") as jsonFile:
			users = json.load(jsonFile)
		del users[un]
		with open("users.json", 'w') as jsonFile:
			json.dump(users, jsonFile)
		input("Account deleted. Press Enter to exit...")
	elif delete == "N" or delete == "n":
		input("Thanks for loggin in. Press Enter to exit...")
	else:
		print("Invalid Input. Please try again.")
		logedin(un)


#login system
def login():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	#check if username is in database
	with open("users.json") as jsonFile:
		userslogin = json.load(jsonFile)
	if un in userslogin:
		if pw == userslogin[un]:
			print("Welcome, " + un + "!")
			logedin(un)
		else:
			print("password is incorrect")
	else:
		print("username not recognized")
#signup system
def signup():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	with open("users.json") as jsonFile:
		users = json.load(jsonFile)
	users[un] = pw
	with open("users.json", 'w') as jsonFile:
		json.dump(users, jsonFile)
	print("You are registered")
	print("Auto logging in...")
	print("Welcome, " + un + "!")
	logedin(un)
#login or sign up
com = input("Login(1) or Signup(2): ")
if com == "1":
	login()
elif com == "2":
	signup()
else:
	print("Invalid input")
	esc = input("Press Enter to exit... ")