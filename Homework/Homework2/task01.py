# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

x = input('Введите вещественное число: ')
from decimal import Decimal
num = Decimal(x)
 
result = num.as_tuple().digits          # .as_tuple  возвращает кортеж со значениями

print(type(result))
print(sum(result))