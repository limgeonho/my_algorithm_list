n = int(input())
arr = list(map(int, input().split()))
visited = [False] * len(arr)
res = [0] * n

def perm(L):
    if L == n:
        print(*res)
        return
    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = arr[i]
        perm(L+1)
        visited[i] = False

# perm(0)

def comb(L, start):
    if L == n:
        print(*res)
        return
    for i in range(start, len(arr)):
        res[L] = arr[i]
        comb(L+1, i+1)

# comb(0, 0)

def perm_with(L):
    if L == n:
        print(*res)
        return
    for i in range(len(arr)):
        res[L] = arr[i]
        perm_with(L+1)

perm_with(0)