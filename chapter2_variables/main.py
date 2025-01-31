# strings - characters sticked to each other
print("--- strings ---")
first_name = "Tristan"
last_name = "Vong"
student_email = "tristan.vong@student.ehb.be"

print("Hello, " + first_name) # concatenated print
print(f"Hello, {first_name} {last_name}") # formatted print
print(f"Your email is {student_email}")

# integers
print("--- integers ---")
age = 19
average_grade_percentage = 65
num1 = 10
num2 = 7
print(f"You are {age} years old")
print(f"Your average grade is: {average_grade_percentage}/100")
print(f"{num1} + {num2} = {num1 + num2}")

# floats
print("--- floats ---")
amount_of_nitrogen = 78.08
price_of_pc = 1079.99
print(f"The air that we breath doesnt consist mostly of oxygen, but nitrogen more specifically around {amount_of_nitrogen}%")
print(f"The price of your personal computer: €{price_of_pc}")

# boolean
print("--- booleans ---")
is_loggedin = True
has_superpowers = False
print(f"logged in? => {is_loggedin}")
print(f"Are you a superhero? => {has_superpowers}")