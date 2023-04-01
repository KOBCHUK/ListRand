import random
start_list = [random.randint(-100,100) for _ in range(12)]
print(start_list)
k = 5
sorted_list = sorted(start_list, reverse=True)
k_element = sorted_list[k - 1]

print(k_element)
