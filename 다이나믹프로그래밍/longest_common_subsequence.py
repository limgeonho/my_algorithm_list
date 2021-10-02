# LCS(최장 공통 부분 수열)
# 두개의 수열이 주어질 때 두 수열의 공통 부분 수열 중 가장 길이가 긴것으로 갱신하면서 구함
# ex) ACAYKP와 CAPCAK => ACAK(4)
# 한 문자씩 비교하면서 문자가 같으면 대각선 위의 값 + 1
# 한 문자씩 비교하면서 문자가 다르면 max(위의 값, 왼쪽 값)

# 비교할 문자열 입력
word_1 = input()
word_2 = input()

n = len(word_1)
m = len(word_2)

# for문을 돌리면서 비교할때 인덱스 값을 맞추기 위해 앞에 빈 문자열 추가
word_1 = ' ' + word_1
word_2 = ' ' + word_2

# 각 문자열을 순회하면서 최대 LCS의 길이!!!를 기록할 dp 생성
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 두 문자열의 문자가 같을 경우 => 이전(i-1, j-1) LCS에서 + 1 (why? : 두 문자열의 공통으로 같은 문자를 만난 것이기 때문에)
        if word_1[i] == word_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        # i와 j-1까지 비교했을때 LCS / i-1과 j까지 비교했을때 LCS => 중 max값을 dp[i][j]에 기록
        # i번째와 j번째가 다른 경우 : [i-1][j]와 [i][j-1] 총 2가지 경우로 나눌 수 있음 => 둘 중 최대값
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# 두 문자열을 전부 순회했을때 마지막이 최대공통부분수열임!
print(dp[n][m])


# ===============================================================================
# LCS를 출력하기
# 기본개념 :  역추적!(LIS에서 한 것 처럼 기록을 하고 거꾸로 탐색해서 올라감)
# LCS를 구하는 과정은 총 3가지 과정으로 분류할 수 있음(1. i, j가 같은 경우 => '1' / 2. dp[i][j-1] > dp[i-1][j] 인 경우 => '2'/ 3. dp[i][j-1] < dp[i-1][j] 인 경우 => '3' )
# 각각의 경우를 order에 기록한다('1', '2', '3')으로 분류해서 기록
word_1 = input()
word_2 = input()

n = len(word_1)
m = len(word_2)

word_1 = ' ' + word_1
word_2 = ' ' + word_2

dp = [[0] * (m+1) for _ in range(n+1)]
# 역추적할 때 사용할 리스트
order = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word_1[i] == word_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            order[i][j] = 1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                dp[i][j] = dp[i][j-1]
                order[i][j] = 2
            else:
                dp[i][j] = dp[i-1][j]
                order[i][j] = 3
# LCS 길이
print(dp[n][m])

# LCS 출력
# 역추적
answer = ''
while n > 0 and m > 0:
    # 마지막부터 거꾸로 역추적 => 기록한 숫자에 맞게 다음 값이 참조 될 수 있도록 n, m을 -= 해준다.
    if order[n][m] == 1:
        answer += word_1[n]
        n -= 1
        m -= 1
    elif order[n][m] == 2:
        m -= 1
    else:
        n -= 1

print(answer[::-1])
