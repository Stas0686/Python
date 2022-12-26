# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

# 1 вар.
def conv_bin_1(number: int):
    result = ""
    while number != 0:
        result = str(number % 2) + result
        number //= 2
    print(f"Вывод в двоичном формате: {result}")
    
conv_bin_1(int(input("Введите число: ")))

# 2 вар.
def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(*list_nums, sep="")


conv_bin(int(input()))
