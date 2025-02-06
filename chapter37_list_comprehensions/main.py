# list comprehensions => concise way to create lists in python
# compact and easier to read

doubled = []
for x in range(1, 11):
    x *= 2
    doubled.append(x)
print(doubled)
print()

doubled_concise = [x * 2 for x in range(1,11)]
print(doubled_concise)