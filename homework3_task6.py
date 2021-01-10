"""Функция, принимающая слова из маленьких латинских букв
и возвращающих их с прописной первой буквой.
"""


def int_func(word):
    for letter in word:
        ru_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        if letter in ru_alphabet:
            print(f"Где-то в слове '{word}' затесались русские буквы..."
                  f"Оно не будет обработано.")
            return None
    if word.islower():
        return word.title()
    else:
        print(f"В слове '{word}' присутствует верхний регистр. "
              "Это слово не будет обработано.")
        return None


words = input("Введите несколько слов латинскими маленькими буквами через пробел: ").split()
new_words = ""

for i in words:
    result = int_func(i)
    if result is not None:
        new_words += (int_func(i) + " ")

print(new_words)
