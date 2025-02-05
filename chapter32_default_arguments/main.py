import time
# start has default value of 0
def count_up(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

# count_up(10)
# count_up(20,15)