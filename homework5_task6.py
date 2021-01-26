result = 0
dictionary = {}
with open("text_6.txt", "r", encoding="utf-8") as my_txt:
    symbols = ["(л)", "(пр)", "(лаб)", "—", ".", "-", ":"]

    for el in my_txt:
        el2 = el
        for symbol in symbols:
            el2 = el2.replace(symbol, "")
        el_words = el2.split()
        result = 0
        for lessons_count in el_words[1:len(el_words)]:
            result += int(lessons_count)
        dictionary[el_words[0]] = result

print(dictionary)
