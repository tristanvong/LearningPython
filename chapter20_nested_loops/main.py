rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Choose a symbol to display: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="") # overwrite end to print chars next to each other default is newline \n
    print()