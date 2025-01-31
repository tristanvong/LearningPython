unit = input("Is this unit in celsius or fahrenheit [C/F]: ")
temperature = float(input("Enter a temperature: "))
converted_temperature = 0 # temp value

if unit == "C":
    converted_temperature = round((temperature * 9/5) + 32, 2)
    print(f"{temperature}{unit} to fahrenheit is: {converted_temperature}F")
elif unit == "F":
    converted_temperature = round((temperature - 32) * 5/9, 2)
    print(f"{temperature}{unit} to celsius is: {converted_temperature}C")
else:
    print(f"{unit} is not a valid unit of temperature")