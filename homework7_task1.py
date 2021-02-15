class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        my_text = ''
        for i in range(0, len(self.my_matrix)):
            my_text += f"{' '.join(map(str, self.my_matrix[i]))}\n"
        return my_text

    def __add__(self, other):
        my_add_matrix = self.my_matrix
        for i in range(0, len(self.my_matrix)):
            for k in range(0, len(self.my_matrix[i])):
                my_add_matrix[i][k] = self.my_matrix[i][k] + other.my_matrix[i][k]
        return Matrix(my_add_matrix)


matrix1 = [[1, 1], [2, 2], [3, 3], [4, 4]]
matrix2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
matrix3 = [[8, 7], [6, 5], [4, 3], [2, 1]]

c1 = Matrix(matrix1)
c2 = Matrix(matrix2)
c3 = Matrix(matrix3)

print(c1 + c2 + c3)
