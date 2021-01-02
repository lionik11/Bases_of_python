user_number_default = int(input("Введите челое число: "))
user_number = user_number_default
figure_max = 0

while user_number != 0:
    figure = user_number % 10
    if figure > figure_max:
        figure_max = figure
    user_number = user_number // 10

print(f"Максимальная цифра в числе {user_number_default} - это {figure_max}.")