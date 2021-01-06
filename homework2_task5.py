my_raiting = [12, 10, 5, 5, 3, 2]
print(my_raiting)

user_input_ = input("Введите натуральное число - это будет новый элемент рейтинга.\n"
                    "Для выхода из ввода нажмите 'q'.\n"
                    "Ваше число: ")

while True:
    if user_input_ == "q":
        print("Ввод данных завершен")
        break
    else:
        user_input = float(user_input_)
        if user_input > my_raiting[0]:
            my_raiting.insert(0, user_input)
            print(my_raiting)
        elif user_input <= my_raiting[-1]:
            my_raiting.append(user_input)
            print(my_raiting)
        else:
            for i in my_raiting:
                if user_input > i:
                    my_raiting.insert(my_raiting.index(i), user_input)
                    print(my_raiting)
                    break
        user_input_ = input("Для выхода из ввода нажмите 'q'. Введите еще число: ")
