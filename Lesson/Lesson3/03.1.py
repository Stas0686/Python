# В файле хранятся числа, нужно выбрать четные и 
# составить список пар (число; квадрат числа). 
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# УПРОЩЕНИЕ с ЛЯМБДАМИ и LIST

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))
print(data)
