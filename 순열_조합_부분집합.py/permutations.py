# 순열구하기

# =========================================================
def permutations_1(L):
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                res[L] = i
                permutations_1(L+1)
                check[i] = 0


n = 3
m = 2
check = [0] * (n+1)
res = [0] * m
permutations_1(0)


# =========================================================

# def permutations_2(i, N):
#     if i == N:
#         print(P)
#     else:
#         for j in range(i, N):
#             P[i], P[j] = P[j], P[i]
#             permutations_2(i+1, N)
#             P[i], P[j] = P[j], P[i]


# P = [1, 2, 3]
# permutations_2(0, len(P))


# # =========================================================
# # 개수가 정해진 순열
# def permutations_3(i, N, r):
#     if i == r:
#         print(P[:i])
#     else:
#         for j in range(i, N):
#             P[i], P[j] = P[j], P[i]
#             permutations_3(i+1, N, r)
#             P[i], P[j] = P[j], P[i]


# P = [1, 2, 3, 4, 5]
# permutations_3(0, len(P), 3)
