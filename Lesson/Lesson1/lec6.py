# Инвертируем число

original = 12345
inverted = 0
while original != 0:
    inverted = inverted*10+(original % 10)
    original //= 10
print(inverted)
