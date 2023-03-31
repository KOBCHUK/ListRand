import random
#numbers = [random.randint(-100,100) for _ in range (12)]
numbers = [1,2,2,4,5,6,6,6,7,8]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print("Original list:", numbers)
print("Unique list:", unique_numbers)