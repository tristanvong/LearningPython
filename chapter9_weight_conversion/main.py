weight = float(input("Enter your weight: "))
unit = input("Is this in kilos or pounds [K/P]")
converted_weight = 0 # temp value

if unit == "K":
    converted_weight = round(weight * 2.20462262185, 2)
    print(f"{weight}kg converted to pounds is: {converted_weight}Lbs")
elif unit == "P":
    converted_weight = round(weight * 0.453592, 2)
    print(f"{weight} pounds converted to kilos is: {converted_weight}kg")
else:
    print(f"{unit} is not a valid unit")