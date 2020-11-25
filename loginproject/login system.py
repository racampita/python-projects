import json
import logedinMod
import loginMod
import signupMod

com = input("Login(1) or Signup(2)? ")
if com == "1":
	loginMod.login()
elif com == "2":
	signupMod.signup()
else:
	print("Invalid input")
	esc = input("Press Enter to exit... ")