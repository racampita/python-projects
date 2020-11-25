import json

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
