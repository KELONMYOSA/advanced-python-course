class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
        result = [[self.matrix[i][j] * other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other):
        if self.columns != other.rows:
            raise ValueError(
                "The number of columns in the first matrix must be equal to the number of rows in the second "
                "for matrix multiplication"
            )
        result = [
            [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)) for j in range(other.columns)]
            for i in range(self.rows)
        ]
        return Matrix(result)
