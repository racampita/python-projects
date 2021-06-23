num1 = int(input("Enter First Number: "))
operation = input("Enter operation: ")
num2 = int(input("Enter Second Number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")

