"""Программа возведения в отрицательную степень положительного числа.
Реализована без оператора '**'.
"""


def my_func(x, y):
    while True:
        if x < 0:
            x = int(input("Исправьтесь. Введите положительное первое число: "))
        elif y > 0 and y == float(y):
            y = int(input("Исправьтесь. Введите целое отрицательное второе число: "))
        else:
            break

    temp = 1
    for i in range(0, abs(y)):
        temp *= x
    result = 1 / temp
    return result


print(my_func(int(input("Введите положительное первое число: ")),
              int(input("Введите целое отрицательное второе число: "))))
