number = 1
goods = []
count = 0
user_input = input("Введите через точку с запятой в следующем порядке 4 элемента: "
                   "название товара, его цену в рублях, количество и единицу измерения: ")

while True:
    if user_input != "q":

        while count != 3:
            count = 0
            for letter in user_input:
                if letter == ";":
                    count += 1

            if count < 3:
                print(f"\nВы ввели слишком мало элементов. Не забудьте проставить разделитель между элементами ';'.")
                user_input = input("Введите через точку с запятой в следующем порядке 4 элемента: "
                                   "название товара, его цену в рублях, количество и единицу измерения: ")
            elif count > 3:
                print("\nВы ввели слишком много элементов. Не забудьте проставить разделитель между элементами ';'.")
                user_input = input("Введите через точку с запятой в следующем порядке 4 элемента: "
                                   "название товара, его цену в рублях, количество и единицу измерения: ")

        user_input_parts = user_input.split(";")
        one_dictionary = {"название": user_input_parts[0], "цена": user_input_parts[1],
                          "количество": user_input_parts[2], "ед": user_input_parts[3]}

        one_tuple = (number, one_dictionary)
        print(one_tuple)
        number += 1
        goods.append(one_tuple)
        user_input = input("\nДавайте добавим следующий элемент. если не хотите, введите 'q'.\n"
                           "Введите через точку с запятой в следующем порядке 4 элемента: "
                           "название товара, его цену в рублях, количество и единицу измерения: ")
    else:
        print("\nВвод данных завершен. Вы ввели следующие элементы: ")
        for element in goods:
            print(element)
        break

names_of_goods = []
for i in goods:
    one_name_of_good = i[1].get("название")
    names_of_goods.append(one_name_of_good)

prices_of_goods = []
for i in goods:
    one_price_of_good = i[1].get("цена")
    prices_of_goods.append(one_price_of_good)

count_of_goods = []
for i in goods:
    one_count_of_good = i[1].get("количество")
    count_of_goods.append(one_count_of_good)

units_of_goods = []
for i in goods:
    one_unit_of_good = i[1].get("ед")
    units_of_goods.append(one_unit_of_good)

analytics_dictionary = {"название": names_of_goods, "цена": prices_of_goods,
                        "количество": count_of_goods, "ед": units_of_goods}

for elements in analytics_dictionary.items():
    print("\n", elements)
