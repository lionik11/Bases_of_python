# Используется файл, соззданный в первом задании
with open("my_txt_1.txt", "r", encoding="utf-8") as my_txt:

    row_count = 0
    words_count = 0
    words_count_all = 0
    symbols = [".", ",", ":", ";", "?", "!", "-"]

    for el in my_txt:
        for symbol in symbols:
            el.replace(symbol, "")
        row_count += 1
        el_words = el.split()
        for el2 in el_words:
            words_count += 1
        print(f"Строка {row_count} содержит {words_count} слов")
        words_count_all += words_count
        words_count = 0
    print(f"Файл {my_txt.name} содержит {row_count} строк, {words_count_all} слов")
