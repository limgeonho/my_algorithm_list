def hoare_p(A, l, r):
    pivot = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def loumuto_p(A, l, r):
    pivot = A[r]
    i = l-1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, l, r):
    if l < r:
        # p = hoare_p(A, l, r)
        p = loumuto_p(A, l, r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    nums = list(map(int, input().split()))

    quick_sort(nums, 0, n-1)

# =========================================================

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def merge_sort(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])
    return merge(left, right)

# array = [1, 5, 8, 41, 2, 68, 4, 5]
array = [2, 3, 1, 4]
print(merge_sort(array))

