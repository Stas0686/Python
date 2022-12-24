# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample


def find_num(count, num):
    if count < 0:
        return "Отрицательное значение количества чисел!"
    # sample - неповторяющиеся значения
    list_nums = sample(range(1, (count + 1) * 2), k=count)
    print(list_nums)

    if num in list_nums:
        return f"Это число - {num} присутствует в списке."
    return f"Это число - {num} не присутствует в списке."


print(find_num(int(input("Введите количество чисел: ")), int(input("Присутствует ли число: "))))

######################### вариант

from random import sample


def find_num(count, num):
    if count < 0:
        return "Отрицательное значение количества чисел(2)!"

    list_nums = sample(range(1, (count + 1) * 2), k=count)
    print(list_nums)
    return "Да" if num in list_nums else "Нет"


print(find_num(int(input("Введите количество чисел(2): ")), int(input("Присутствует ли число(2): "))))