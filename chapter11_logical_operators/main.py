temperature = 23
is_raining = False

if temperature > 35 or temperature < 0 or is_raining:
    print(f"The outdoor party is cancelled")
else:
    print(f"The outdoor party is still scheduled")

temperature2 = 2
is_sunny = False

if temperature2 >= 28 and is_sunny:
    print("It is hot weather and sunny outside")
elif temperature2 <= 0 and is_sunny:
    print("It is cold outside and sunny")
elif 28 > temperature2 > 0 and is_sunny:
    print("It is warm outside and sunny")
elif temperature2 >= 28 and not is_sunny:
    print("It is hot weather and cloudy outside")
elif temperature2 <= 0 and not is_sunny:
    print("It is cold outside and cloudy")
elif 28 > temperature2 > 0 and not is_sunny:
    print("it is warm outside and cloudy")