c, d = 4, 5       # множественное присвоение
a = (3, 4)       # кортеж (если только один аргумент, то после него нужно оставить запятую!)
b = (5, 6, 7)
print(a)
print(c, d)

for item in b:
    print(item)
##########################################
t = tuple(['red', 'green', 'blue'])         # создаем список и конвертируем его в кортеж
red, green, blue = t                        # распаковываем его и превращаем его в независимые переменные
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blu