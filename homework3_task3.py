"""Функция, возвращающая сумму двух наибольших аргументов.
Вариант 1.
"""


def my_func(var_1, var_2, var_3):
    my_vars = [var_1, var_2, var_3]
    return sum(my_vars) - min(my_vars)


try:
    var_a = int(input("Посчитаем сумму двух наибольших чисел из трёх.\nВведите первое число: "))
    var_b = int(input("Введите второе число: "))
    var_c = int(input("Введите третье число: "))
    print(f"Сумма двух наибольших чисел равна {my_func(var_a, var_b, var_c)}.")

except ValueError:
    print("Вы ввели не число. Попробуйте сначала.")
