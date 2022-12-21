# Запись в файл
with open('file.txt', 'w') as data:
 data.write('line 1\n')
 data.write('line 2\n')

# Запись в файл
colors = ['red', 'green', '!@#$%4334567']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()

# Чтение из файла
path = 'file.txt'
data = open(path, 'r')
for line in data: 
 print(line)
data.close()
