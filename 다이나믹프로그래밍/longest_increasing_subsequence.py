from bisect import bisect_left
# 최장 부분 증가 수열 알고리즘
# 임의의 수열이 주어졌을 경우 순차적으로 임의의 숫자들을 뽑았을 때 만든 수열이 오름차순으로 정렬되어 있고 길이가 가장 긴 수열
# 1. DP를 이용해서 푼다.
# 2. 이분탐색을 이용해서 푼다.

# ======================================================================
# 1. DP를 이용해서 푼다.

array = [3, 1, 2, 4, 8, 6, 7]
n = len(array)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

result = max(dp)


# ======================================================================
# 2. 이분탐색을 이용해서 푼다.
# 이분탐색을 이용한 방법은 입력 값이 커도 빠르게 계산이 가능 끝...

array = [3, 1, 2, 4, 8, 6, 7]
n = len(array)
dp = [array[0]]

for i in range(1, n):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        dp[bisect_left(dp, array[i])] = array[i]

result = len(dp)
print(dp)

# ======================================================================
# 3. 그러면 해당 LIS에 포함되는 숫자들을 직접 구하는 방법!!!!!!!
# dp를 구하는 방법까지는 동일함
# max(dp)를 order에 넣고 거꾸로 탐색하면서 order과 같은 인덱스의 숫자를 list에 넣고
# for문을 거꾸로 탐색하면서 order을 -1씩 해준다.

array = [3, 1, 2, 4, 8, 6, 7]
n = len(array)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

order = max(dp)

answer = []

for i in range(n-1, -1, -1):
    if dp[i] == order:
        answer.append(array[i])
        order -= 1

print(*answer[::-1])
