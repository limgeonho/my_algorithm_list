# 선택 정렬 알고리즘
# 처음부터 자신을 제외한 다음 숫자들을 순회하면서 가장 작은 수를 찾은 다음에 위치를 swap한다.
# 다음 인덱스로 이동해서 반복

def selection_sort(array):
    for i in range(len(array)):

        # 맨 처음 순환하는 인덱스를 기준으로 잡는다
        min_index = i

        # 기준점 다음 인덱스부터 순회한다.
        for j in range(i+1, len(array)):

            # 기준 인덱스 값보다 작은 값이 나타나면 작은 인덱스 값을 갱신한다.
            if array[j] < array[min_index]:
                min_index = j
        # 인덱스 순환이 종료되면 기준점과 가장 작은 인덱스 값을 가지는 원소를 swap한다.
        array[i], array[min_index] = array[min_index], array[i]

    return array


array = [1, 5, 8, 1, 3, 9, 4]

print(selection_sort(array))
# [1, 1, 3, 4, 5, 8, 9]
