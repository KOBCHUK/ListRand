import random
list_1 = [1, 2, 3, 4, 7, 9, 10, 12, 14, 15, 18, 20]
list_2 = [3, 4, 5, 6, 8, 7, 9, 11, 12, 13, 14, 15]
#list_1 = [random.randint (-100,100) for _ in range (12)]
#list_2 = [random.randint (-100,100) for _ in range (12)]
same_n = []

for n in list_1:
    if n in list_2 and n not in same_n:
        same_n.append(n)

print(same_n)
