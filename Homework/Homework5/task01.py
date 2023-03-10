# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

text = "xyz"
print("Слово которое нужно удалить из текста: ", text)
num_word = (int(input("Количество слов в тексте: ")))
list_word = []
print("Текст: ")
for x in range(num_word):
    random_txt = random.sample(text, 3)
    list_word.append("".join(random_txt))

print(" ".join(list_word))

print("Текст без xyz: ")
list_word2 = list(filter(lambda x: text not in x, list_word))
print(" ".join(list_word2))