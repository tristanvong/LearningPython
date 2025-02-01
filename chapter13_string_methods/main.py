# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")
# result = len(name) # returns length of characters of a string
# result = name.find(" ") # find first occurrence of given character
# result = name.rfind("o") # find last occurrence of given character
# name = name.capitalize() # used to make first word in given string capitalized
# name = name.upper() # make all string characters uppercase
# name = name.lower() # make all string characters lowercase
# name = name.isdigit() # returns true if string only consists of integers otherwise false
# name = name.isalpha() # returns true if string has only alphabetic characters otherwise false
# result = phone_number.count("-") # returns count of given character
# phone_number = phone_number.replace("-", " ") # replace a character by another
# print(phone_number)

# print(help(str)) # prints all the string methods

# Exercise: validate user input
# the username must not be more than 12 chars
# username must not contain spaces
# username must not contain digits
username = input("Enter an username: ")
if len(username) > 12:
    print("Your username is too long. Your username must be under 12 characters.")
if username.count(" ") != 0:
    print("Your username must not contain a whitespace")
if not username.isalpha():
    print("Your username must not contain any digits and only alphabetic characters")
if len(username) <= 12 and username.count(" ") == 0 and username.isalpha():
    print(f"Welcome to the program {username}")