# 구간합 기법
# 리스트의 연속된 특정 구간의 합을 빠르게 구하는 방법
# 데이터의 개수 n과 데이터 입력 받기
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 리스트 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# prefix_sum 리스트
# [0, 10, 30, 60, 100, 150]

# 구간 합 계산 (2번째 수부터 3번째 수까지) => 2번째 수 + 3번째 수
# 3번째 수까지의 합 - 1번째 수까지의 합 = 2, 3번째 수들의 합
# prefix_sum[3] = 3번째 수까지의 합
# prefix_sum[1] = 1번째 수까지의 합

right = 3
left = 1
print(prefix_sum[right] - prefix_sum[left - 1])
