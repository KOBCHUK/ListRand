#import random
#start_list = [random.randint(-100,100) for _ in range (12)]
start_list = [1,2,2,4,5,6,6,6,7,8]
unique_numbers = []
for n in start_list:
    if n not in unique_numbers:
        unique_numbers.append(n)

print("Start list:", start_list)
print("Unique list:", unique_numbers)