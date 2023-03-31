import random

numbers = [random.randint(-100, 100) for _ in range(10)]

even_numbers = [n for n in numbers if n % 2 == 0]

odd_numbers = [n for n in numbers if n % 2 != 0]

negative_numbers = [n for n in numbers if n < 0]

positive_numbers = [n for n in numbers if n > 0]

print("List of random integers:", numbers)
print("List of even numbers:", even_numbers)
print("List of odd numbers:", odd_numbers)
print("List of negative numbers:", negative_numbers)
print("List of positive numbers:", positive_numbers)
