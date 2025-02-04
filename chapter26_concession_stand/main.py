menu = {
    "pizza": 6.00,
    "hotdog": 3.40,
    "hamburger": 10.20,
    "popcorn": 6.00,
    "fries": 4.00,
    "chips": 8.80,
    "soda": 2.00
}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to stop)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")