import random

numbers = [random.randint(-100, 100) for _ in range(12)]

even_count = len([n for n in numbers if n % 2 == 0])
odd_count = len([n for n in numbers if n % 2 != 0])

print("List of random integers:", numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
