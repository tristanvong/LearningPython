# input function, that grabs user input and returns it as a string

name = input("Enter your name: ")
age = input("Enter your age: ")
name = name.strip() # remove whitespace before and after user input
age = int(age) # convert to integer because cannot use math on string
# age = int(input("Enter your age: ")) would also work
age_next_year = age + 1

print(f"Hello, {name}. You are {age} years old.")
print(f"Next year, you'll be {age_next_year} years old.")

# exercise 1 : area of rectangle program
print("--- area of rectangle-calculator 2000 ---")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
result = length * width
print(f"The area of the rectangle with the length of {length} and width of {width} = {result}")

# exercise 2 : shopping cart program
item = input("Enter an item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("How many items would you like to buy: "))
total_price = price * quantity

print(f"You are buying {item} the amount you selected: {quantity}")
print(f"The total price is €{total_price}")