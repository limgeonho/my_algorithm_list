# n_queen 알고리즘(백트래킹)
# queen이 서로 공격할 수 없는 위치를 하나씩 놓아 나가는 문제
# 대표적인 백트래킹 문제
# 놓아 나가면서 기존 조건에 위배되는 위치이후는 확인하지 않고 back!!

# ===========================================================================================
def is_available(candidate, current_col):
    current_row = len(candidate)  # 선택된 queen list의 길이, 개수 = 현재 행의 위치
    for queen_row in range(current_row):
        # 세로줄 탐색 or 대각선 탐색(2가지임) => 이 조건문이 핵심!
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


# current_row : 현재 행 / current_candidate : 현재까지 선택된 queen
def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    # current_row에서 한 칸씩 오른쪽으로 이동하며 queen을 놓을 자리를 선택
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):  # 대각선, 세로 여부 파악
            current_candidate.append(candidate_col)  # 하나의 queen을 선택하고 후보에 넣음
            DFS(N, current_row + 1, current_candidate, final_result)  # 다음줄로 넘어감
            current_candidate.pop()  # 아직 남은 후보를 확인하기 위해 마지막 후보를 pop하고 나머지 순회


def solve_n_queens(N):  # 체스판 크기입력(n*n)
    final_result = []   # n-queen이 가능한 queen들의 위치
    DFS(N, 0, [], final_result)
    print(len(final_result))
    return


# ===========================================================================================


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


# ===========================================================================================
# list의 참/거짓 유무만 확인하면되기 때문에 연산속도가 빠름

def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True


def calc(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row, col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans


n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)
print(calc(0))
