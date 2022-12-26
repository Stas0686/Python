# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.


def check(str_list: list):
    new_list = []
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if str_list[i].replace("-", "").isdigit():
            new_list.append(str_list[i])
    return new_list
    

def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print("Данные неверны")
    return []


print(*find_max_min(input("Введите числа через пробел: ")))
