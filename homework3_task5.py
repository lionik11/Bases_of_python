"""Программа рассчитывания суммы вводимых чисел до момента ввода специального символа,
который завершит ввод.
"""


def my_func():
    my_var = input("Введите несколько чисел через пробел, "
                   "я посчитаю их сумму.\nДля завершения введите 'q'. "
                   "Допускается ввести 'q' через пробел после чисел.\n").split()
    result = 0
    while True:
        try:
            int_my_var = []
            for i in my_var:
                if i != "q":
                    digit_number = int(i)
                    int_my_var.append(digit_number)
                else:
                    break
            iteration_sum = sum(int_my_var)
            result += iteration_sum
            print(f"{iteration_sum}({result})")
            if "q" not in my_var:
                my_var = input("\nВведите еще несколько чисел через пробел, если хотите.\n"
                               "Я добавлю их сумму к уже посчитанной.\nДля завершения введите 'q'. "
                               "Допускается ввести 'q' через пробел после чисел.\n").split()
            else:
                return result

        except ValueError:
            print(f"Как минимум один из элементов - не число. Попробуйте еще раз.\n"
                  f"Ваша текущая сумма: {result}")
            my_var = input("\nВведите несколько чисел через пробел, "
                           "я посчитаю их сумму.\nДля завершения введите 'q'. "
                           "Допускается ввести 'q' через пробел после чисел.\n").split()


print(f"Итоговая сумма равна {my_func()}.")
