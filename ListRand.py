import random

start_list = [random.randint(-100,100) for _ in range(12)]
min_index = start_list.index(min(start_list))
max_index = start_list.index(max(start_list))

print(start_list)

start_list[min_index], start_list[max_index] = start_list[max_index], start_list[min_index]

print(start_list)
