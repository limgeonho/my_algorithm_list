# 부분집합 구하기(DFS 사용)
# 1. itertools 이용
# 2. 비트마스크 이용
# 3. 재귀함수 이용

# ========================================================================
# 1. itertools 이용
from itertools import combinations

array = [1, 2, 3]
N = len(array)

for n in range(N+1):
    # n == 부분집합 원소의 개수
    subsets = combinations(array, n)
    for subset in subsets:
        print(subset)

# ========================================================================
# 2. 비트마스크 이용
array = [1, 2, 3]
n = len(array)

for i in range(1 << n):
    res = []
    for j in range(n):
        if i & (1 << j):
            res.append(array[j])
    print(res)

# ========================================================================
# 3. 재귀함수 이용(1)
# 노드를 하나씩 내려갈 때마다 선택여부를 0, 1로 표시한다. => 재귀
# 마지막노드까지 내려가면 check리스트를 확인하여 선택된 인자의 index만 출력 후 다시 뒤로 돌아가서 순회


def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)


n = 3
check = [0] * (n+1)
DFS(1)


# ======================================================
# 3. 재귀(완전탐색)(2)
array = [1, 2, 3]
subset = []


def comb(idx):
    global total

    if idx == len(array):
        print(subset)
        return

    subset.append(array[idx])
    comb(idx+1)

    subset.pop()
    comb(idx+1)


comb(0)
