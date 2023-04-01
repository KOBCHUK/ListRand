import random

start_list = [random.randint(-100,100) for _ in range (12)]

positiv_list = [n for n in start_list if n > 0]

print(start_list)
print(positiv_list)