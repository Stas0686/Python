# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def list_of_prime_factors(N):
    factors = list()
    divisor = 2
    while (divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N/divisor
        else:
            divisor += 1
    return factors

print(list_of_prime_factors(int(input("Введите число: "))))
