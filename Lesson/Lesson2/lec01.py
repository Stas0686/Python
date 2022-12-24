# Запись в файл
with open('file.txt', 'a') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# Запись в файл
colors = ['red', 'green', '!@#$%4334567']
data = open('file.txt', 'a')
data.writelines(colors)  # разделителей не будет
data.close()             # разрываем связь

# Чтение из файла
path = 'file.txt'       # путь к файлу
data = open(path, 'r')  # открытие в режиме чтения
for line in data:       # через цикл идем по файлу
    print(line)         # считываем строки
data.close()            # разрываем связь
