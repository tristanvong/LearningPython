# Simple addition calculator

number = float(input("Enter number to add to addition (0 to stop): "))
total = 0
while number != 0:
    total += number
    number = float(input("Enter number to add to addition (0 to stop): "))
else:
    print(f"Total of additions is: {total}")