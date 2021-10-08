# 에라토스테네스의 체
# 임의의 수보다 작은 소수들을 구하는데 유용
# 2부터 N까지의 모든 자연수를 나열
# 남은 수들 중에서 가장 작은 수를 제외하고 해당 작은 수의 배수들을 모두 제외한다
# 반복

# 구하려는 소수의 범위
n = 1000

# n이하의 모든 수의 리스트에 True를 할당한다
array = [True for i in range(n+1)]

# 에라토스테네스의 체(범위만 주의)
for i in range(2, int(n**0.5)+1):

    # 남아 있는 가장 작은 수는 True
    if array[i] == True:

        # 배수 곱셈을 하기 위한j => *2, *3, *4 ...
        j = 2

        # n보다 작거나 같을 때까지 계속해서 곱셈 누적 후 곱해진 수는 False로 바꾼다.(체로 거르기)
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
