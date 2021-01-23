import json

sum_profit = 0
cnt = 0
dictionary = {}

with open("text_7.txt", "r", encoding="utf-8") as my_txt:
    for el in my_txt:
        cnt += 1
        el_words = el.split()
        profit = float(el_words[2]) - float(el_words[3])
        sum_profit += profit
        dictionary[el_words[0]] = profit

av_profit = sum_profit / cnt

my_list = [dictionary, {"average_profit": av_profit}]

with open("my_json.json", "w") as write_f:
    json.dump(my_list, write_f)
