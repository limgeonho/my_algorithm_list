# n_queen 알고리즘(백트래킹)
# queen이 서로 공격할 수 없는 위치를 하나씩 놓아 나가는 문제
# 대표적인 백트래킹 문제
# 놓아 나가면서 기존 조건에 위배되는 위치이후는 확인하지 않고 back!!

# 총 queen을 놓는 횟수가 체스판의 길이와 같을 때 까지 DFS
def n_queens(col, i):
    n = len(col) - 1
    if (promising(col, i)):
        if (i == n):
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(col, i + 1)


# 대각선과 같은 열에 있는 지 확인
def promising(col, i):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag


n = 8
col = [0] * (n + 1)
n_queens(col, 0)
