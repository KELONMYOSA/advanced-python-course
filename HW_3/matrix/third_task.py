from typing import ClassVar

from HW_3.matrix.first_task import Matrix


class MatrixHashMixin:
    def __hash__(self):
        # Считаем сумму всех элементов матрицы и возвращаем её
        return sum(sum(row) for row in self.matrix)


class CachedMatrixMultiplicationMixin:
    _cache: ClassVar[dict] = {}

    def __matmul__(self, other):
        hash_key = hash(self) ^ hash(other)
        if hash_key in self._cache:
            return self._cache[hash_key]
        else:
            result = super().__matmul__(other)
            self._cache[hash_key] = result
            return result


class Matrix(MatrixHashMixin, CachedMatrixMultiplicationMixin, Matrix):
    pass
