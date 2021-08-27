# rotate_matrix_2 => 행렬(2차원 리스트) 돌리기(90도)
# 1. 기존에 함수형으로 만들어서 사용하던 방법
# 2. zip을 이용한 간단한 방법
# 차이점 :  (1)번은 중복해서 실행하면 90, 180, 270, 360도 회전 + 값을 변경 O
# 차이점 :  (2)번은 90도 까지만 (1)번과 같음 + 값을 변경 X
# 결론 : 90도만 회전하는 경우(세로방향 탐색을 위해) + 값을 단순하게 조회만 하는 경우(값 변경X)에는 그냥 (2)번 => list(zip(*array))사용하자


# 1. 기존에 함수형으로 만들어서 사용하던 방법
def rotate_matrix_by_90_degree_2(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]

    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


array_1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
array_1 = rotate_matrix_by_90_degree_2(array_1)
array_1 = rotate_matrix_by_90_degree_2(array_1)
print(array_1)


# 2. zip을 이용한 간단한 방법
array_2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
array_2 = list(zip(*array_2))
array_2 = list(zip(*array_2))
print(array_2)
