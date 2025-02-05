import random
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in dice:
    total += die
print(f"The total is: {total} you threw: {dice}")