# 행렬 곱하기 알고리즘
# 3중 for문이라서 시간 복잡도가 상당함...
# 행렬의 곱셈은 예를들면 2x3 * 3x2 => 2x2 이런식으로 결과가 나타남

def multiply_matrix(arr1, arr2):
    # 곱해질 행렬의 row
    row = len(arr1)

    # 곱해질 행렬의 column
    column = len(arr2[0])

    # 곱해질 행렬의 기본설정
    answer = [[0]*column for _ in range(row)]

    # 행렬 곱하기
    for i in range(row):
        for j in range(column):
            # 이후 부터는 새로운 i행j열짜리 행렬을 만들면서 두 행렬의 곱을 넣어준다. k의 범위는 len(arr1[0])이거나 len(arr2)여도 된다.
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
