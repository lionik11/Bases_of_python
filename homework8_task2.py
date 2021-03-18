class ZeroError(Exception):
    def __str__(self):
        return "Делить на 0 нельзя..."


h = input("Введите через пробел два числа для деления первого на второе: ")
h = h.split(" ")
a = float(h[0])
b = float(h[1])
while True:
    try:
        if b == 0:
            raise ZeroError
        else:
            print(f"Результат деления: {round(a / b, 2)}")
            break
    except ZeroError as err:
        print(err)
        b = float(input("Введите другой делитель: "))
