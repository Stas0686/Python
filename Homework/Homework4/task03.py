# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.

# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random

def list_rand_nums(count, min=1, max=10):
    if count <= 0:
        print("Неверное значение количества чисел!")
        return []

    list_nums = [random.randint(min, max)]
    for i in range (1, count):
        list_nums.append(random.randint(min, max)) 

    return list_nums

all_list = list_rand_nums(int(input("Введите количество чисел: ")))
print(all_list)

print("Уникальные числа: ") 
for k in all_list: 
    if all_list.count(k) == 1: 
        print(k, end = " ")
        


### Хотел как то так решить, но не понял как это сделать ###

# from collections import defaultdict
# from collections import Counter
# A = [1 ,2 ,3 ,2 ,5, 1]
# counter = Counter(A)
# countmap = defaultdict(list)
# for k, v in counter.iteritems():
#     countmap[v].append(k)
# print (countmap [v])

