import numpy as np

from HW_3.matrix.third_task import Matrix


def find_collision(target_hash, exclude):
    while True:
        candidate = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
        if hash(candidate) == target_hash and candidate != exclude:
            return candidate


def find_matrices():
    while True:
        matrix_a = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
        matrix_b = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

        target_hash = hash(matrix_a)
        matrix_c = find_collision(target_hash, matrix_a)

        matrix_ab = matrix_a @ matrix_b
        matrix_cd = matrix_c @ matrix_b

        if matrix_ab != matrix_cd:
            return matrix_a, matrix_b, matrix_c, matrix_b


def write_matrix_to_file(matrix, path):
    with open(path, "w") as f:
        f.write(str(matrix))


if __name__ == "__main__":
    matrix_a, matrix_b, matrix_c, matrix_d = find_matrices()

    matrix_ab = matrix_a @ matrix_b
    matrix_cd = matrix_c @ matrix_d

    write_matrix_to_file(matrix_a, "./artifacts/3.3/A.txt")
    write_matrix_to_file(matrix_b, "./artifacts/3.3/B.txt")
    write_matrix_to_file(matrix_c, "./artifacts/3.3/C.txt")
    write_matrix_to_file(matrix_d, "./artifacts/3.3/D.txt")
    write_matrix_to_file(matrix_ab, "./artifacts/3.3/AB.txt")
    write_matrix_to_file(matrix_cd, "./artifacts/3.3/CD.txt")

    with open("./artifacts/3.3/hash.txt", "w") as f:
        f.write(f"Hash of AB: {hash(matrix_ab)}\n")
        f.write(f"Hash of CD: {hash(matrix_cd)}\n")
