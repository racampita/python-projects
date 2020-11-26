import logedinMod
import json
import os

def login(trial = 0):
	os.system('cls')
	un = input("Enter Username: ")
	pw = input("Enter Password: ")
	#check if username is in database
	with open("users.json") as jsonFile:
		users = json.load(jsonFile)
	if un in users:
		if pw == users[un]:
			logedinMod.logedin(un)
		else:
			if trial >= 5:
				input("You have no more trials. Press ENTER to exit...")
			else:
				
				input("Password is incorrect." +"You have "+ str(5-trial) + " more trials."  + " Press ENTER to try again...")
				trial = trial + 1
				login(trial)
	else:
		print("username not recognized")