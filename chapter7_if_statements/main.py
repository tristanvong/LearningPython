age = int(input("Enter your age: "))

if age < 18:
    print("You are not allowed to use this program.")
elif age <= 100:
    print("You are allowed to use this program.")
else:
    print("You are certainly allowed to use this program.")

response = input("Would you like food? [Y/N]: ")
if response == "Y":
    print("Magically printing some artificial food...")
elif response == "N":
    print("Not printing food. Closing program.")
else:
    print("Invalid option chosen.")

response_name = input("Enter your name: ")
if response_name == "":
    print(f"Invalid input, you did not enter your name")
else:
    print(f"Hello {response_name}")

is_student = True
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")