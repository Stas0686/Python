# Рекурсивная Фибоначчи

def fib(n):
    if n in [1, 2]:
        return 1                        # если попадаем в 1ый или 2ой элемент возвращаем "1"
    else:
        return fib(n-1) + fib(n-2)      # иначе возвращаем рекусивный метод для n-1 и n-2
    
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34
