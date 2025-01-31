# type casting => converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Tristan Vong"
age = 19
average_grade = 65.24
is_student = True

# use type function to know the type of variable
print(type(name))

average_grade_integer = int(average_grade)
print(average_grade_integer)

age_float = float(age)
print(f"original age integer: {age} => age as float: {age_float}")

# the result of "age_string" will look the same as the output of integer age,
# this is why type function is used to know for sure what the data type is
age_string = str(age)
print(f"original age integer: {age} {type(age)}, age as string: {age_string} {type(age_string)}")

# this will result True if string contains a value "a" "tristan" ... if its empty => False
name_bool = bool(name)
print(name_bool)