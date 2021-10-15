n = int(input())
array = list(map(int, input().split()))
check = [False] * len(array)
res = [0] * n

def perm(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        if check[i]:
            continue
        check[i] = True
        res[L] = array[i]
        perm(L+1)
        check[i] = False

perm(0)

print('==================')

def comb(L, start):
    if L == n:
        print(*res)
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        comb(L+1, i+1)

comb(0, 0)

print('==================')

def perm_2(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        res[L] = array[i]
        perm_2(L+1)

perm_2(0)
