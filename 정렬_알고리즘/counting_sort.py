# 카운팅 알고리즘
# 나열 된 수들의 개수를 카운팅 한 후 앞에서 부터 숫자와 해당 카운팅 횟수만큼 출력한다.
# (주의) 카운팅해야하는 array의 크기와 count리스트의 크기는 같지 않을 수 도 있다
# count리스트의 크기는 array 중 가장 큰 수 만큼 만들고 초기값을 0으로 세팅한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# array의 최대값보다 하나 큰 수 만큼 리스트를 만든다
count = [0] * (max(array)+1)

# count리스트 안에 array에서 나온 숫자들을 +1해주면서 누적한다.
for i in range(len(array)):
    count[array[i]] += 1

# 인덱스를 해당 인덱스가 카운팅된 만큼 반복하며 출력한다.
for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')
