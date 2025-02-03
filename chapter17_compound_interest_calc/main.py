import math

principle = 0
rate_of_interest = 0
time = 0 # In years

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print(f"Principle can not be negative or zero, you entered: {principle}")

while rate_of_interest <= 0:
    rate_of_interest = float(input("Enter the rate of interest amount: "))
    if rate_of_interest <= 0:
        print(f"The rate of interest can not be negative or zero, you entered: {rate_of_interest}")

while time <= 0:
    time = float(input("Enter the time (years) amount: "))
    if time <= 0:
        print(f"The time (years) can not be negative or zero, you entered: {time}")

total = principle * math.pow((1 + rate_of_interest / 100), time)
print(f"Balance after {time} years: ${total}")