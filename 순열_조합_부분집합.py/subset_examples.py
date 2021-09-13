# 부분집합 구하기
# 1<<n => 부분집합의 개수(n개의 원소일 때) = 1 * (2**n)

# arr = [1, 2, 3, 4, 5, 6]
arr = [1, 2, 3]
n = len(arr)

# range(1 << n) => 공집합 포함, range(1, 1 << n) => 공집합 미포함
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print((i, j), arr[j], end=' ')

    print()
