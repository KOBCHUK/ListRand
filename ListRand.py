import random

start_list = [random.randint(-100,100) for _ in range(12)]
square_list =[]
for n in start_list :
    square_list.append(n ** 2)

print(start_list)
print(square_list)
