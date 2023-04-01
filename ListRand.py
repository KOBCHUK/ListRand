import random

start_list = [random.randint(-100, 100) for _ in range(12)]

negative_sum = sum([n for n in start_list if n < 0])

even_sum = sum([n for n in start_list if n % 2 == 0])

odd_sum = sum([n for n in start_list if n % 2 != 0])

multiple_of_3 = 1
for i in range(len(start_list)):
    if i % 3 == 0:
        multiple_of_3 *= start_list[i]

min_index = start_list.index(min(start_list))
max_index = start_list.index(max(start_list))
if min_index > max_index:
    min_index, max_index = max_index, min_index
between_min_max = 1
for i in range(min_index+1, max_index):
    between_min_max *= start_list[i]

positive_element = [i for i in range(len(start_list)) if start_list[i] > 0]
if len(positive_element) >= 2:
    first_positive_element = positive_element[0]
    last_positive_element = positive_element[-1]
    between_first_last_sum = sum(start_list[first_positive_element+1:last_positive_element])

print("List of random integers:", start_list)
print("Sum of negative numbers:", negative_sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Product of elements with indices multiples of 3:", multiple_of_3)
print("Product of elements between minimum and maximum element:", between_min_max)
print("Sum of elements between the first and last positive element:", between_first_last_sum)
