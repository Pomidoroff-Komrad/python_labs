# ЗАМЕЧАНИЕ: примеры задания проходят; добавь докстринг с описанием ValueError.
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Матрица рваная")

    transpose_mat = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        transpose_mat.append(new_row)
    return transpose_mat

test_array_1 = [
    [[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2], [3, 4]],
    [],
    [[1, 2], [3]]
]
for mat in test_array_1:
    print(transpose(mat))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    sums = []
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Матрица рваная")
        sums.append(sum(row))
    return sums

test_array_2 = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]],
]

#for mat in test_array_2:
#    print(row_sums(mat))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    sums = []
    if len(mat) == 0:
        return []

    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Матрица рваная")

    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        sums.append(s)
    return sums

test_array_3 = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]],
]

#for mat in test_array_3:
#    print(col_sums(mat))
