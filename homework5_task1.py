with open("my_txt_1.txt", "w", encoding="utf-8") as my_txt:
    while True:
        user_input = input("Введите какой-нибудь текст для документа. "
                           "Для завершения - ничего не вводите и просто нажмите 'Enter'.\n")
        if user_input != "":
            print(user_input, file=my_txt)
        else:
            break
