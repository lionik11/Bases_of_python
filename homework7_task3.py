class Cell:
    def __init__(self, mini_cells_count):
        self.mini_cells_count = mini_cells_count

    def __str__(self):
        return f"Mini cells count: {self.mini_cells_count}"

    def __add__(self, other):
        mini_cells_count_plus = self.mini_cells_count + other.mini_cells_count
        return Cell(mini_cells_count_plus)

    def __sub__(self, other):
        if self.mini_cells_count < other.mini_cells_count:
            raise ValueError("The difference between the cells is less than zero")
        mini_cells_count_minus = self.mini_cells_count - other.mini_cells_count
        return Cell(mini_cells_count_minus)

    def __mul__(self, other):
        mini_cells_count_multiplication = self.mini_cells_count * other.mini_cells_count
        return Cell(mini_cells_count_multiplication)

    def __truediv__(self, other):
        mini_cells_count_truediv = self.mini_cells_count // other.mini_cells_count
        return Cell(mini_cells_count_truediv)

    def make_order(self, cells_in_row):
        order = ''
        for i in range(0, (self.mini_cells_count // cells_in_row)):
            order += '*' * cells_in_row + '\n'
        return order + '*' * (self.mini_cells_count % cells_in_row)


cl1 = Cell(12)
cl2 = Cell(31)
cl3 = Cell(14)

common_cell_plus = cl1 + cl2 + cl3
print(common_cell_plus)

common_cell_minus = cl1 + cl2 - cl3
print(common_cell_minus)

common_cell_multiplication = cl1 * cl2 * cl3
print(common_cell_multiplication)

common_cell_truediv = cl2 / cl3
print(common_cell_truediv)

print(f"cl1:\n{cl1.make_order(8)}\n-\ncl2:\n{cl2.make_order(10)}\n-\ncl3:\n{cl3.make_order(6)}")
