import logedinMod
import json

def signup():
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	with open("users.json") as jsonFile:
		users = json.load(jsonFile)
	if un in users:
		print("This username already exists. Please try a different one.")
		signup()
	else:
		users[un] = pw
		with open("users.json", 'w') as jsonFile:
			json.dump(users, jsonFile)
		print("You are registered")
		print("Auto logging in...")
		print("Welcome, " + un + "!")
		logedinMod.logedin(un)