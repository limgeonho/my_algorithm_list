# 기본중의 기본 순열, 조합, 중복순열 / 부분집합 => 재귀문제 거의 해결

n = int(input())
array = list(map(int, input().split()))

visited = [False] * len(array)
res = [0] * n


# ====================================
# 순열
def perm(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = array[i]
        perm(L+1)
        visited[i] = False

# perm(0)


# ====================================
# 중복순열
def perm_with(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        res[L] = array[i]
        perm_with(L+1)

# perm_with(0)


# ====================================
# 조합
def comb(L, start):
    if L == n:
        print(*res)
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        comb(L+1, i+1)

# comb(0, 0)


# ====================================
# 부분집합
def subset(L, ss):
    if L == n:
        if not ss:                  # 공집합은 제거
            return
        print(ss)
        return
    subset(L+1, ss + [array[L]])  # 해당 원소를 선택 O
    subset(L+1, ss)               # 해당 원소를 선택 X

# subset(0, [])
