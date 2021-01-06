user_input = input("Введите несколько слов, разделенных пробелами: ")

for ind, el in enumerate(list(user_input.split())):
    print(ind, el[:10])
