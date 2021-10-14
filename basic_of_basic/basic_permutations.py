# 기본중의 기본 순열, 조합, 중복순열

N, M = map(int, input().split())

path = [0 for _ in range(N)]
used = [0 for _ in range(7)]


# 중복순열
def run1(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1, 7):
        path[lev] = i
        run1(lev+1)


# 조합
def run2(lev, start):
    if lev == N:
        print(*path)
        return
    for i in range(start, 7):
        path[lev] = i
        run2(lev+1, i)

# 순열


def run3(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1, 7):
        if used[i] == 1:
            continue
        used[i] = 1
        path[lev] = i
        run3(lev + 1)
        used[i] = 0


if M == 1:
    run1(0)
elif M == 2:
    run2(0, 1)
elif M == 3:
    run3(0)


# ========================================================================
# def type1(t):
#     if t == n:
#         print(*arr)
#         return
#     for i in range(1, 7):
#         arr.append(i)
#         type1(t+1)
#         arr.pop()

# def type2(t, num):
#     if t == n:
#         print(*arr)
#         return
#     for i in range(num, 7):
#         arr.append(i)
#         type2(t+1, i)
#         arr.pop()

# def type3(t):
#     if t == n:
#         print(*arr)
#         return
#     for i in range(1, 7):
#         if used[i]:
#             continue
#         arr.append(i)
#         used[i] = 1
#         type3(t+1)
#         arr.pop()
#         used[i] = 0

# n, m = map(int, input().split())

# arr = []
# used = [0] * 7
# if m == 1:
#     type1(0)
# elif m == 2:
#     type2(0, 1)
# elif m == 3:
#     type3(0)
