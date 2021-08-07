import heapq

# heapq(힙)
# 힙은 기본적으로 최소힙으로 설계되어 있음
# 하지만 최대힙을 구하기 위해서는 원소의 부호를 임시적으로 바꿨다가 꺼낸 뒤에 다시 부호를 바꿔준다.
# heappush(), heappop()
# 다익스트라 알고리즘에서 사용

# =============================================================================================
# 기본 최소 힙


def heapsort_default(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = heapsort_default([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# =============================================================================================
# 최대 힙 - value를 heapq에 넣을 때 부호를 반대로 -> 다시 꺼낼 때 부호를 반대로


def heapsort_max(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


result = heapsort_max([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# =============================================================================================
