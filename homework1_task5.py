revenue = float(input("Введите выручку Вашей фирмы в тысячах рублей: "))
costs = float(input("Введите издержки Вышей фирмы в тысячах рублей: "))
profit = revenue - costs

if profit > 0:
    profitability = (profit / revenue * 100)
    print(f"Ваша фирма работает с прибылью {profit} тыс. руб. Рентабельность фирмы равна {profitability:.2f}%.")
    workers_count = int(input("Введите численность сотрудников Вашей фирмы: "))
    profit_to_workers = (profit / workers_count)
    print(f"В расчете на одного сотрудника Ваша фирма имеет прибыль {profit_to_workers:.2f} тыс. руб./чел.")
elif profit < 0:
    print(f"Ваша фирма работает с убытками: {profit} тыс. руб.")
else:
    print("Ваша фирма не имеет прибыли, но и работает без убытков.")
