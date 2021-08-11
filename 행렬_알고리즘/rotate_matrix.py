# 행렬 90도로 회전시키기 알고리즘

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def rotate_matrix_by_90_degree(a):
    # 기존 행렬의 행과열의 순서를 바꿔야한다 : 행, 열 => 열, 행
    row_length = len(a)
    column_length = len(a[0])

    # 새로운 행렬의 기본 설정(기존의 행렬과는 반대)
    res = [[0] * row_length for _ in range(column_length)]

    # 오른쪽 위에서 부터 하나씩 아래로 채워나감
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


print(rotate_matrix_by_90_degree(a))
# [
# [9, 5, 1],
# [10, 6, 2],
# [11, 7, 3],
# [12, 8, 4]
# ]
