# 이진탐색(재귀함수로 구현)
# target 수를 입력 받고 리스트안에서 target의 위치를 반환하는 방법
# 이진탐색을 하기 위해서는 리스트가 정렬이 되어 있는게 전제되어야 한다.

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

# =====================================================================
# 이진탐색(반복문으로 구현)


def binary_search(array, target, start, end):
    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
