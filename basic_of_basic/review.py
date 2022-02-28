n = int(input())
array = list(map(int, input().split()))

visited = [False] * len(array)
res = [0] * n

# def perm(L):
#     if L == n:
#         print(res)
#         return
#
#     for i in range(len(array)):
#         if visited[i]:
#             continue
#         visited[i] = True
#         res[L] = array[i]
#         perm(L+1)
#         visited[i] = False
#
# perm(0)
#
#
# def comb(L, start):
#     if L == n:
#         print(res)
#         return
#     for i in range(start, len(array)):
#         res[L] = array[i]
#         comb(L+1, i+1)
#
# comb(0, 0)

# def perm_with(L):
#     if L == n:
#         print(res)
#         return
#     for i in range(len(array)):
#         res[L] = array[i]
#         perm_with(L+1)
#
# perm_with(0)

def subset(L, ss):
    if L == n:
        if not ss:
            return
        print(ss)
        return
    subset(L+1, ss + [array[L]])
    subset(L+1, ss)

subset(0, [])


def next_perm(array):
    i = len(array)-1
    while i > 0 and array[i-1] >= array[i]:
        i -= 1

    if i < 0:
        return False

    j = len(array) - 1
    while array[i-1] >= array[j]:
        j -= 1

    array[i-1], array[j] = array[j], array[i-1]

    j = len(array) - 1
    while i > j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    return True