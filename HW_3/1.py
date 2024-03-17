import numpy as np

from HW_3.matrix.first_task import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    add_result = matrix1 + matrix2
    mul_result = matrix1 * matrix2
    matmul_result = matrix1 @ matrix2

    with open("./artifacts/3.1/matrix+.txt", "w") as f:
        f.write(str(add_result))

    with open("./artifacts/3.1/matrix＊.txt", "w") as f:
        f.write(str(mul_result))

    with open("./artifacts/3.1/matrix@.txt", "w") as f:
        f.write(str(matmul_result))
