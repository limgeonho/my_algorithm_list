# 선택 정렬
# 처음부타

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


array = [1, 5, 8, 1, 3, 9, 4]

print(selection_sort(array))
# [1, 1, 3, 4, 5, 8, 9]
