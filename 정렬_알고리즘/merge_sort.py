# 병합정렬
# 리스트를 반으로 계속 나눠서 더 이상 나눌 수 없는 곳까지 나눔 => 재귀이용
# 나눈 리스트를 하나씩 비교하면서 정렬하고 합침 => 반복
# O(nlongn)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 - right 데이터가 없을 때
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
