import json
import logedinMod
import loginMod
import signupMod
import os

os.system('cls')
com = input("Login(1) or Signup(2)? ")
if com == "1":
	loginMod.login()
elif com == "2":
	signupMod.signup()
else:
	print("Invalid input")
	input("Press Enter to exit... ")
	os.system('cls')