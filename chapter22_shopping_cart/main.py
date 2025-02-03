foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

total = 0
for price in prices:
    total += price

products = ""
for food in foods:
    if foods.index(food) != len(foods)-1:
        products += food + ", "
    else:
        products += food

print("--- Your Cart: ---")
print(f"You are buying the following products: {products}")
print(f"Your total is {total}")