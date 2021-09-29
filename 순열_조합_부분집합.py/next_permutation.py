# 다음순열, 이전순열, 모든순열 구하는 방법
# 주어진 순열이 어떤 순열의 마지막 순열인지 첫 순열인지 판단해야함
# 첫 순열 : 오름차순
# 마지막 순열 : 내림차순


# =====================================================================
# 다음순열
# 다음순열 구하는 방법
# 1. 리스트를 거꾸로 탐색하면서 array[i-1] < array[i] 까지 계속 i-=1하면서 탐색한다.(특정순열의 마지막 순열을 찾기 위함)
# 2. i값을 구했다면 array[i-1]보다 오른쪽에 있는 수들 중 큰 값중에 가장 작은 수를 찾는다
# 3. array[i-1]과 array[j]를 swap
# 4. array[i]부터 마지막 수까지 오름차순 정렬

def next_permutations(array):

    i = len(array) - 1  # i는 거꾸로 순회
    while i > 0 and array[i-1] >= array[i]:  # 앞에 있는 수가 뒤에 있는 수보다 작은 경우 i 찾기
        i -= 1

    if i <= 0:  # i가 0보다 작거나 같으면 마지막순열이기 때문에 끝(탐색필요 X)
        return False

    j = len(array) - 1  # j도 거꾸로 순회
    while array[j] <= array[i-1]:  # array[j]가 array[i-1]보다 큰 경우 찾기
        j -= 1

    array[i-1], array[j] = array[j], array[i-1]  # swap

    j = len(array) - 1  # j값 초기화 => i이후 부분을 오름차순으로 정렬하기 위해
    while i < j:  # 계속 swap
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return True


# array = [7, 2, 3, 6, 5, 4, 1]
# next_permutations(array)
# print(array)  # [7, 2, 4, 1, 3, 5, 6]


# =====================================================================
# 이전순열
# 다음순열의 부등호만 반대로 해주면 끝
def prev_permutations(array):
    i = len(array) - 1
    while i > 0 and array[i-1] <= array[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(array) - 1
    while array[j] >= array[i-1]:
        j -= 1

    array[i-1], array[j] = array[j], array[i-1]

    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i -= 1
        j -= 1
    return True


array = [7, 2, 3, 6, 5, 4, 1]
prev_permutations(array)
print(array)  # [7, 2, 3, 6, 5, 1, 4]


# =====================================================================
# 모든순열
# 맨처음에 해당 순열을 한 번 출력하고(do-while가 파이썬에 없음 ㅜ)
# next_permutations을 계속 출력
array_all = [1, 2, 3]
print(array_all)
while True:
    if next_permutations(array_all):
        print(array_all)
    else:
        break

# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
