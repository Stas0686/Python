# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

import random
a = int(input('Введите число: '))
my_list = [i for i in range(a)]
print("Мой список : " + str(my_list))
res = random.sample(my_list, len(my_list))
print("Новый список : " + str(res))
