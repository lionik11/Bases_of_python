from functools import reduce


def my_func(el1, el2):
    return el1 * el2


my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(my_list)
print(reduce(my_func, my_list))
