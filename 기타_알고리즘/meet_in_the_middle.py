# meet in the middle
# 문제의 수가 너무 큰 경우 완전 탐색을 한다면 => 시간초과
# 따라서, 절반으로 나눈다
# 각각의 절반을 따로 계산해서 합친다
# 따로 코드가 정리되어 있는 것이 아니라 문제의 범위를 보고 나눠서 각각 구한다음 처리하는 아이디어만...

# 예시문제 : (BOJ_1208 : 부분수열의 합2)
# 해당문제는 수의 범위가 매우 큼... => 반반 나눠서 해결(meet in the middle)
n, s = map(int, input().split())
a = list(map(int, input().split()))

# 반반 나누는 과정
m = n//2
n = n-m

# first group
first = [0]*(1 << n)
for i in range(1 << n):
    for k in range(n):
        if (i & (1 << k)) > 0:
            first[i] += a[k]


# second group
second = [0]*(1 << m)
for i in range(1 << m):
    for k in range(m):
        if (i & (1 << k)) > 0:
            second[i] += a[k+n]

# 각각 오름차순 정렬
first.sort()
second.sort()
# second group는 거꾸로 뒤집기 => 두 group을 각각 돌면서 모든 경우의 수를 구할 때 한 쪽 방향으로 진행하기위함
second.reverse()

n = (1 << n)
m = (1 << m)
i = 0
j = 0
ans = 0

while i < n and j < m:
    # 합이 s와 같은지 확인
    if first[i] + second[j] == s:
        c1 = 1
        c2 = 1
        i += 1
        j += 1
        # 같다면 앞 뒤에 같은 수가 또 존재하는 지 확인
        while i < n and first[i] == first[i-1]:
            c1 += 1
            i += 1
        # 같다면 앞 뒤에 같은 수가 또 존재하는 지 확인
        while j < m and second[j] == second[j-1]:
            c2 += 1
            j += 1
        # 해당 경우의 수 누적
        ans += c1*c2
    # 합이 s보다 작다면 first group만 이동(합이 커짐 : first group 오름차순)
    elif first[i] + second[j] < s:
        i += 1
    # 합이 s보다 크다면 second group만 이동(합이 작아짐 : second group 내림차순)
    else:
        j += 1
if s == 0:
    ans -= 1
print(ans)

# 결론 : 수가 너무 크기 때문에 => meet in the middle기법을 통해 수를 작게 분할
# => two pointer을 활용해서 해당 경우를 찾음
