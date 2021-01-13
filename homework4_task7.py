def fact(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
        yield result


user_n = int(input("Введите целое число для расчета факториала: "))

g = fact(user_n)
print(g)

for el in g:
    print(el)
