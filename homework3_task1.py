"""Функция, принимающая два числе и выполняющая их деление."""


def divide(number1, number2):
    try:
        result = int(number1) / int(number2)
        print(f"Частное (округлено до двух знаков после запятой): {round(result, 2)}")
    # Обработка ошибки ввода числа
    except ValueError:
        print("Вы ввели некорректное число!")
    # Обработка деления на ноль
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


number1_user = input("Введите делимое: ")
number2_user = input("Введите делитель: ")

print("Функция деления первого вводимого числа на второе число.")
divide(number1_user, number2_user)
