import random
start_list = [random.randint(-100,100) for _ in range(12)]
print(start_list)
average = sum(start_list) / len(start_list)
print(average)
quantity = 0

for n in start_list:
    if n > average:
        quantity += 1

print(quantity)
