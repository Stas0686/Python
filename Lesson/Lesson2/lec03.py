def concatenatio(*params):
    res: str = ""                       # прописывается тип данных
  # res = ""                            # можно тип данных не указывать
  # res: int = 0                        # для работы с числами (не)
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
print(concatenatio('1', '2', '3', '4'))  # 1234
