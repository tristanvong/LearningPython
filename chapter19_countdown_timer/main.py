import time

chosen_time = int(input("Enter an amount to seconds to wait: "))
for x in range(chosen_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print(f"Your alarm went of you've waited for {chosen_time} seconds")