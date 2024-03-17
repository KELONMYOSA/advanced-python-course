import numpy as np


class MatrixBase:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix(np.add(self.matrix, other.matrix))

    def __mul__(self, other):
        return Matrix(np.multiply(self.matrix, other.matrix))

    def __matmul__(self, other):
        return Matrix(np.dot(self.matrix, other.matrix))

    def __str__(self):
        return np.array_str(self.matrix)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = np.array(value)


class MatrixIO:
    def to_file(self, path):
        with open(path, "w") as f:
            for line in str(self).splitlines():
                f.write(line + "\n")


class Matrix(MatrixBase, MatrixIO):
    pass
