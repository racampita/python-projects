import logedinMod
import json

def login():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	#check if username is in database
	with open("users.json") as jsonFile:
		userslogin = json.load(jsonFile)
	if un in userslogin:
		if pw == userslogin[un]:
			print("Welcome, " + un + "!")
			logedinMod.logedin(un)
		else:
			print("password is incorrect")
	else:
		print("username not recognized")