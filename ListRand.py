import random

numbers = [random.randint(-100, 100) for _ in range(10)]

negative_sum = sum([n for n in numbers if n < 0])

even_sum = sum([n for n in numbers if n % 2 == 0])

odd_sum = sum([n for n in numbers if n % 2 != 0])

multiple_of_3_product = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        multiple_of_3_product *= numbers[i]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
if min_index > max_index:
    min_index, max_index = max_index, min_index
between_min_max_product = 1
for i in range(min_index+1, max_index):
    between_min_max_product *= numbers[i]

positive_indices = [i for i in range(len(numbers)) if numbers[i] > 0]
if len(positive_indices) >= 2:
    first_positive_index = positive_indices[0]
    last_positive_index = positive_indices[-1]
    between_first_last_sum = sum(numbers[first_positive_index+1:last_positive_index])

print("List of random integers:", numbers)
print("Sum of negative numbers:", negative_sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Product of elements with indices multiples of 3:", multiple_of_3_product)
print("Product of elements between minimum and maximum element:", between_min_max_product)
if len(positive_indices) >= 2:
    print("Sum of elements between the first and last positive element:", between_first_last_sum)
