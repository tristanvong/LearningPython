fruits = ["apple", "banana", "orange", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
for grocery in groceries:
    print(grocery)
    for item in grocery:
        print(item)

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for item in row:
        print(item, end=" ")
    print()