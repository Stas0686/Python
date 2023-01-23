# Вывод четных чисел от 1 до 20


list = []
for i in range(1, 21):
    if (i % 2 == 0):
        list.append(i)
print(list)


list = [i for i in range(1, 21) if i % 2 == 0]
print(list)
