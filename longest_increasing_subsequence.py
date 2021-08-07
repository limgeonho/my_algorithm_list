from bisect import bisect_left
# 최장 부분 증가 수열 알고리즘
# 임의의 수열이 주어졌을 경우 순차적으로 임의의 숫자들을 뽑았을 때 만든 수열이 오름차순으로 정렬되어 있고 길이가 가장 긴 수열
# 1. DP를 이용해서 푼다.
# 2. 이분탐색을 이용해서 푼다.

# ======================================================================\
# 1. DP를 이용해서 푼다.

array = [3, 1, 2, 4, 8, 6, 7]
n = len(array)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

result = max(dp)


# ======================================================================\
# 2. 이분탐색을 이용해서 푼다.
# 이분탐색을 이용한 방법은 입력 값이 커도 빠르게 계산이 가능하고 LIS또한 직접 구할 수 있다.(사용 권장)

array = [3, 1, 2, 4, 8, 6, 7]
n = len(array)
dp = [array[0]]

for i in range(1, n):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        dp[bisect_left(dp, array[i])] = array[i]

result = max(dp)
print(dp)
