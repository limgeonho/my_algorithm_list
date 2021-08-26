# 병합정렬
# 리스트를 반으로 계속 나눠서 더 이상 나눌 수 없는 곳까지 나눔 => 재귀이용
# 나눈 리스트를 하나씩 비교하면서 정렬하고 합침 => 반복
# O(nlongn)

def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)


def merge(left_array, right_array):
    merged_array = []
    while len(left_array) > 0 or len(right_array) > 0:

        if len(left_array) > 0 and len(right_array) > 0:

            if left_array[0] <= right_array[0]:
                merged_array.append(left_array[0])
                left_array.pop(0)
            else:
                merged_array.append(right_array[0])
                right_array.pop(0)

        elif len(left_array) > 0:
            merged_array.append(left_array[0])
            left_array.pop(0)

        elif len(right_array) > 0:
            merged_array.append(right_array[0])
            right_array.pop(0)

    return merged_array


# array = [1, 5, 8, 41, 2, 68, 4, 5]
array = [2, 3, 1, 4]
print(merge_sort(array))
