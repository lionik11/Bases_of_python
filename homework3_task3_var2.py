"""Функция, возвращающая сумму двух наибольших аргументов.
Вариант 2.
"""


def my_func():
    my_var = input("Введите три числа через пробел: ").split()
    while True:
        if len(my_var) > 3:
            my_var = input("Вы ввели слишком много чисел. Введите три числа через пробел: ").split()
        elif len(my_var) < 3:
            my_var = input("Вы ввели слишком мало чисел. Введите три числа через пробел: ").split()
        else:
            break

    try:
        int_my_var = []
        for i in my_var:
            digit_number = int(i)
            int_my_var.append(digit_number)
        return sum(int_my_var) - min(int_my_var)

    except ValueError:
        print("Как минимум один из трёх элементов - не число. Попробуйте сначала.")


result = my_func()
if result is not None:
    print(f"Сумма двух наибольших чисел равна {result}")
