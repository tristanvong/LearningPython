# iterables = object/collection that can return its items one at a time, so it can be iterated over in a loop
list_nums = [1,2,3,4,5,6]
for x in list_nums:
    print(x)
print()

tuple_cars = ("bmw", "honda", "toyota", "ford")
for x in tuple_cars:
    print(x)
print()

set_fruits = {"apple", "banana", "pineapple"}
for x in set_fruits:
    print(set_fruits)
print()

full_name = "Tristan Vong"
for char in full_name:
    print(char)
print()

dictionary_grades = {
    "course1": 56.8,
    "course2": 77.0,
    "course3": 47.20,
    "course4": 38.90,
    "course5": 93.34
}

for key in dictionary_grades:
    print(key)
print()

for value in dictionary_grades.values():
    print(value)
print()

for key, value in dictionary_grades.items():
    print(f"{key} = {value}")