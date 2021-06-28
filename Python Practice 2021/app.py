real_number = 568
tries = 0
while tries < 3:
    number = int(input("Guess: "))
    if number > real_number:
        print("Lower")
    elif number < real_number:
        print("Higher")
    elif number == real_number:
        print("You are correct!")
        break
    tries += 1
else:
    print("You failed...")