# 투 포인터 기법
# 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
# start점부터 end점까지 사이에 있는 원소들을 전부 포함
# #
# =============================================================================
# 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다
# 현재 부분 합이 M과 같다면, 카운트한다
# 현재 부분 합이 M보다 작다면, end를 1 증가시킨다
# 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다
# 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다
# =============================================================================


# n은 데이터의 개수, m은 찾고자 하는 부분 합
n = 5
m = 5
data = [1, 2, 3, 2, 5]

cnt = 0
interval_sum = 0
end = 0

# Two-pointer
for start in range(n):
    # 부분합이 목표합보다 작을때 end += 1
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # 부분합과 목표합이 같을때 cnt += 1
    if interval_sum == m:
        cnt += 1

    # 부분합이 목표합보다 크거나 같다면
    interval_sum -= data[start]

print(cnt)

# =============================================================================
# n은 데이터의 개수, s는 찾고자 하는 부분 합


n, s = map(int, input().split())
data = list(map(int, input().split()))

left = right = 0
sum = data[0]
cnt = 0

while left <= right and right < n:
    # 구간합이 목표합보다 작은 경우 => right증가
    if sum < s:
        right += 1
        if right < n:
            sum += data[right]
    # 구간합이 목표합과 같은 경우 => 카운팅 + right증가
    elif sum == s:
        cnt += 1
        right += 1
        if right < n:
            sum += data[right]
    # 구간합이 목표합보다 큰 경우 => 구간합에서 현재 left값을 빼고 left증가
    elif sum > s:
        sum -= data[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = data[left]

print(cnt)
