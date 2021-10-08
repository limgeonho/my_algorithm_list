# 퀵 정렬
# 리스트의 가장 첫 수를 pivot로 선택하고 pivot를 기준으로 작은 수는 왼쪽, 큰 수는 오륵쪽으로 넣는다
# 반복하면 리스트가 계속 쪼개진다 -> 길이가 1이하인 리스트는 return
# 결국 마지막에 전부 쪼개지고 pivot에 의해 나눠진 리스트들을 하나로 합치면서 return
def quick_sort(array):
    if len(array) <= 1:
        return array

    left = []
    right = []
    pivot = array[0]

    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


array = [1, 5, 7, 4, 2, 385, 1, 23, 84, 21, 3]

print(quick_sort(array))


# ======================================================================================
# 위의 방법은 파이썬에서만 가능함


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


array = [1, 5, 7, 4, 2, 385, 1, 23, 84, 21, 3]
quick_sort(array, 0, len(array)-1)
