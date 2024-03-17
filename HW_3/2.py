import numpy as np

from HW_3.matrix.second_task import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    add_result = matrix1 + matrix2
    mul_result = matrix1 * matrix2
    matmul_result = matrix1 @ matrix2

    add_result.to_file("./artifacts/3.2/matrix+.txt")
    mul_result.to_file("./artifacts/3.2/matrix＊.txt")
    matmul_result.to_file("./artifacts/3.2/matrix@.txt")
