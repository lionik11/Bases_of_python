underpaid_workers = []
sum_salary = 0
count_workers = 0

with open("text_3.txt", "r", encoding="utf-8") as my_txt:

    for el in my_txt:
        el_words = el.split(",")
        sum_salary += float(el_words[1])
        count_workers += 1
        if float(el_words[1]) < 20000:
            print(f"{el_words[0]} получает {el_words[1][:-1]} руб.")

print(f"Все вышеперечисленные сотрудники получают меньше 20000 руб.\n"
      f"Средняя зарплата всех сотрудников составляет {round((sum_salary / count_workers), 1)} руб.")
