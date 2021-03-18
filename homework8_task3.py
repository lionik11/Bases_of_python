class NotDigitError(Exception):
    def __str__(self):
        return "Введенный элемент не является числом"


my_list = []

while True:
    try:
        print(my_list)
        k = input("Для выхода из программы введите 'stop'. Введите число для его добавления в список: ")
        if k == "stop":
            break
        elif k.isdigit():
            my_list.append(int(k))
        else:
            raise NotDigitError
    except NotDigitError as err:
        print(err)
