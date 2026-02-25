# def outer(x):
#     def inner():
#         return round(x)
#     return inner


# result = outer(10.5)
# print(result())


def make_adder(n):
    def add(x):
        return x + n
    return add


add5 = make_adder(5)
print(add5(10))