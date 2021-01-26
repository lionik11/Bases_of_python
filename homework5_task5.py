from random import randint
numbers = [randint(1, 200) for i in range(15)]

with open("my_txt_5.txt", "w", encoding="utf-8") as my_txt:
    for i in numbers:
        print(f"{i} ", file=my_txt, end="")

with open("my_txt_5.txt", "r", encoding="utf-8") as my_txt:
    for el in my_txt:
        el_list = el.split()
        result = 0
        for number in el_list:
            result += int(number)
    print(f"Сумма чисел в документе {my_txt.name} равна {result}")
