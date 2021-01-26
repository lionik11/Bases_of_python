my_dictionary = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

my_translated_txt = open("text_4_translated.txt", "w", encoding="utf-8")

with open("text_4.txt", "r", encoding="utf-8") as my_txt:
    for el in my_txt:
        el_words = el.split()
        translated_word = my_dictionary.get(el_words[0].lower())
        print(f"{translated_word.title()} {el_words[1]} {el_words[2]}", file=my_translated_txt)

my_translated_txt.close()
