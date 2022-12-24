dictionary = {}             # словари
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }


print(dictionary)               # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])       # ←
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)                    # вывод ключей

for k in dictionary.values():
    print(k)                    #  вывод значений

for k in dictionary:
    print(dictionary[k])        #  вывод значений
