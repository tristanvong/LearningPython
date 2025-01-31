import math

friends = 0

friends = friends + 1
friends += 1

friends = friends -2
friends -= 2

friends = friends * 3
friends *= 3

friends = friends / 2
friends /= 2

friends = friends ** 2
friends **= 2

remainder = friends % 2

print(friends)

x = 3.14
y = -4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(2, 3)
# result = max(x, y, z)
# result = min(x, y, z)

# pi = math.pi
# euler = math.e
# result = math.sqrt(25)
# result_ceiled = math.ceil(9.1) # round up => 10
# result_floored = math.floor(9.9) # round down => 9

# Circumference of a circle program
user_radius = float(input("Enter the radius of the circle: "))
pi = math.pi
result = 2 * pi * user_radius
print(f"The circumference of the circle with given radius is: {round(result, 2)}")

# Hypotenuse calculator program
user_side1 = math.pow(float(input("Enter side a: ")), 2)
user_side2 = math.pow(float(input("Enter side b: ")), 2)
result_hypotenuse = math.sqrt(user_side1 + user_side2)
print(f"The hypotenuse for the given triangle is: {round(result_hypotenuse, 2)}")