import random

start_list = [random.randint(-100, 100) for _ in range(12)]

even = len([n for n in start_list if n % 2 == 0])
odd = len([n for n in start_list if n % 2 != 0])

print("List of random integers:", start_list)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
