# 전치행렬 만들기 => 딱히 알고리즘은 아님
# 가로세로 값 찾아낼때 헷갈리면 사용
# 전치행렬로 변환을 통해 세로로 탐색하는 것을 가로로 바꿔버림
array = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def transposed_matrix(array):
    row = len(array)
    col = len(array[0])
    changed_array = [[0]*(row) for _ in range(col)]

    for i in range(row):
        for j in range(col):
            changed_array[j][i] = array[i][j]
    return changed_array


print(transposed_matrix(array))
# [[1, 1, 1], [2, 2, 2], [3, 3, 3]]


# ================================================================================
def transposed_matrix(array):
    n = len(array)
    changed_array = [[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            changed_array[i][j] = array[j][i]
    return changed_array


print(transposed_matrix(array))
# [[1, 1, 1], [2, 2, 2], [3, 3, 3]]


# ================================================================================
# 너무 간단한 방법...
T = list(zip(*array))
print(T)
# [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
