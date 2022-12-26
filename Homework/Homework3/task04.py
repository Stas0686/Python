# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

# Вар. 1
lst = list(map(float, input("Введите вещественные числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
max = max(new_lst)
min = min(new_lst)
print(f"Max: {max}")
print(f"Min: {min}")
diff = max - min
print(f"Difference: {diff}")


# Вар. 2
from random import uniform


def list_rand_nums(count: int):
    list_nums = []
    if count <= 0:
        print("Неверное значение количества чисел!")
        return [0.0]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums


def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
    return result


all_list = list_rand_nums(int(input("Введите количество чисел: ")))
print(all_list)
print(dif_max_min(all_list))