from sys import argv

script_name, work_time, working_rate, prize = argv

salary = int(work_time) * int(working_rate) + int(prize)

print(f"Выработка в часах - {work_time};\nСтавка в час - {working_rate} руб.;"
      f"\nПремия - {prize} руб.;\n\nЗарплата равна {salary} руб.")
