my_list = []
user_input = input("Вам нужно ввести любые значения для создания списка.\n"
                   "Для завершения ввода введите 'q'\n\nВедите любое значение: ")
while True:
    if user_input == "q":
        print("Ввод данных завершен")
        break
    else:
        my_list.append(user_input)
        user_input = input("Введите еще значение: ")

print(f"Вы ввели список {my_list}")

i = 1
while i < len(my_list):
    my_list.insert(i - 1, my_list[i])
    my_list.pop(i + 1)
    i += 2

print(f"После преобразования получился список {my_list}")
