class ComplexNumber:
    x: complex

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = complex(a, b)

    def __str__(self):
        return str(self.x)

    def __mul__(self, other):
        mul_complex_number = self.x * other.x
        mul_a = mul_complex_number.real
        mul_b = mul_complex_number.imag
        return ComplexNumber(mul_a, mul_b)

    def __add__(self, other):
        mul_complex_number = self.x + other.x
        mul_a = mul_complex_number.real
        mul_b = mul_complex_number.imag
        return ComplexNumber(mul_a, mul_b)


my_class1 = ComplexNumber(1, 2)
my_class2 = ComplexNumber(2, 3)
my_class3 = ComplexNumber(3, 1)

print(f"Класс 1: {my_class1};")
print(f"Класс 2: {my_class2};")
print(f"Класс 3: {my_class3};")
print(f"Сумма 1 и 2: {my_class1 + my_class2};")
print(f"Сумма 1, 2, 3: {my_class1 + my_class2 + my_class3}")
print(f"Произведение 1 и 2: {my_class1 * my_class2};")
print(f"Произведение 1, 2, 3: {my_class1 * my_class2 * my_class3}")
