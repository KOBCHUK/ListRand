list_1 = [1, 2, 3, 4, 7, 9, 10, 12, 14, 15, 18, 20]
list_2 = [3, 4, 5, 6, 8, 7, 9, 11, 12, 13, 14, 15]
same_n = []

for n in list_1:
    if n in list_2 and n not in same_n:
        same_n.append(n)
print(list_1)
print(list_2)
print("List without duplicates", same_n)
