# LCS(최장 공통 부분 수열)
# 두개의 수열이 주어질 때 두 수열의 공통 부분 수열 중 가장 길이가 긴것으로 갱신하면서 구함
# ex) ACAYKP와 CAPCAK => ACAK(4)
# 한 문자씩 비교하면서 문자가 같으면 대각선 위의 값 + 1
# 한 문자씩 비교하면서 문자가 다르면 max(위의 값, 왼쪽 값)
word_1 = input()
word_2 = input()

dp = [[0]*(len(word_2)+1) for _ in range(len(word_1)+1)]

for i in range(1, len(word_1)+1):
    for j in range(1, len(word_2)+1):
        if word_1[i-1] == word_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(word_1)][len(word_2)])
