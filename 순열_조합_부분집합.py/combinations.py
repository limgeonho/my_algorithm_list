# 조합구하기


def combinations_1(L, start):
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
    else:
        for i in range(start, n+1):
            res[L] = i
            combinations_1(L+1, i+1)


n = 3
m = 2
res = [0] * m
combinations_1(0, 1)
