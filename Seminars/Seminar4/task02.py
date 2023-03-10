# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.


# 1 вариант

from math import sqrt
def discr(a, b, c):
    D = b**2-4*a*c
    with open("diskr.txt", "a", encoding="utf-8") as file:
        file.write(f"{a}x² + {b}x + {c} = 0\n")
        if D > 0:
            x1 = (-b+sqrt(D))/(2*a)
            x2 = (-b-sqrt(D))/(2*a)
            file.write(f"{x1}, {x2}\n")
        elif D == 0:
            x = -b/(2*a)
            file.write(f"{x}\n")
        else:
            file.write("Нет корней\n")
discr(2, 3, 1)

# Красивое решение

from math import sqrt


def roots_equ(a, b, c):
    d = b ** 2 - 4 * a * c
    with open("roots.txt", "a", encoding="utf-8") as my_f:
        my_f.write(f"{a}x ** 2 + {b}x + {c}\n")
        if d > 0 and a:
            my_f.write(f"Первый корень: {(-b + sqrt(d)) / (2 * a):.2f}\n")
            my_f.write(f"Второй корень: {(-b - sqrt(d)) / (2 * a):.2f}\n")
        elif d == 0 and a:
            my_f.write(f"Корень: {-b / (2 * a):.2f}\n")
        else:
            my_f.write("Нет корней.\n")


# 1 2 -3, 5 6 -7, 8 9 -10
for i in range(3):
    roots_equ(int(input("Введите коэффициент 'a': ")), 
              int(input("Введите коэффициент 'b': ")),
              int(input("Введите коэффициент 'c': ")))