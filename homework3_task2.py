"""Функция, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
"""


def user_data(name, surname, birth_year, mail, phone, city):
    print(f"\nВас зовут {name} {surname}.\n"
          f"Вы родились в {birth_year} году и сейчас проживаете в городе {city}.\n"
          f"Ваш e-mail: {mail}, номер телефона: {phone}.")


user_data(surname=input("Введите фамилию: "), name=input("Введите имя: "), city=input("Введите город проживания: "),
          mail=input("Введите e-mail: "), phone=input("Введите номер телефона: "),
          birth_year=input("Введите год рождения: "))
