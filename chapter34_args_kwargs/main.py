# args = multiple/varying non keyword arguments => put into a tuple
# kwargs = multiple/varying keyword arguments => put into a dictionary
def addition(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(addition(3, 8, 0, 9, 12))
print()
def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "Bluesquare Street",
              house_number = 384,
              postal_code = 4300,
              city = "Waremme",
              country = "Belgium")