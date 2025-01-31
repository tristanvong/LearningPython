# Simple calculator program
# do math on two numbers with given operator

operator = input("Enter an operator: (+ - * /): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
result = 0 #temp

if operator == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif operator == "/":
    result = num1 / num2
    print(f"The result is {result}")
else:
    print(f"{operator} is not a valid operator")