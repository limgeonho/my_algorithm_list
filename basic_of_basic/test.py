n = int(input())
# 숫자 리스트
num = list(map(int, input().split()))
# 저장 공간
path = [0 for _ in range(n)]
used = [False for _ in range(len(num))]

# lev 시작점
def permutation(lev):
    if lev == n:
        print(*path)
        return
    for i in range(len(num)):
        if used[i]:
            continue
        used[i] = True
        path[lev] = num[i]
        permutation(lev + 1)
        used[i] = False

permutation(0)

print('==================================')

def combination(L, start):
    if L == n:
        print(*path)
        return
    for i in range(start, len(num)):
        path[L] = num[i]
        combination(L+1, i+1)

combination(0, 0)


print('==================================')

def permutation_with(L):
    if L == n:
        print(*path)
        return
    for i in range(len(num)):
        path[L] = num[i]
        permutation_with(L+1)

permutation_with(0)