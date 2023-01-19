def mult(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))


calc(mult, 4, 5)

calc (lambda x, y: x*y, 4, 5)