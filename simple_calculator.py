try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

except:
    print("Enter valid numbers")
    exit()


operation = input("Choose the operation you want to perform +, -, /, x : ")


if operation == "+":
    result = num1 + num2 
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "x":
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
elif operation == "/":
    if num2 == 0:
        print("Math Error, Cannot divide by Zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
