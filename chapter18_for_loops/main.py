for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)): # reversed function makes the for loop in opposite order
    print(x)

name = "Tristan_Vong"
for x in name:
    print(x)

for x in range (1, 21):
    if x == 13:
        continue # skips iteration 13
    print(x)

for x in range(1, 101):
    if x == 50:
        break # stops for loop at iteration 50
    print(x)