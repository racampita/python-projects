import json

def logedin(un):
	delete = input("Do you want to delete your account? (Y/N)")
	if delete == "Y" or delete == "y":
		while True:
			confirmation = input ("Enter your password: ")
			with open("users.json") as jsonFile:
				users = json.load(jsonFile)
			#password authentication
			if confirmation == users[un]:
				del users[un]
				with open("users.json", 'w') as jsonFile:
					json.dump(users, jsonFile)
				input("Account deleted. Press Enter to exit...")
				break
			else:
				print("Password is incorrect.")
	elif delete == "N" or delete == "n":
		input("Thanks for loggin in. Press Enter to exit...")
	else:
		print("Invalid Input. Please try again.")
		logedin(un)
