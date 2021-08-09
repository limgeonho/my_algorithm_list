# 버블 정렬 알고리즘
# 앞에서부터 순차적으로 바로 다음 숫자와 비교한 뒤 큰 숫자와 작은 숫자의 순서를 교환해 나가는 알고리즘

def bubble_sort(array):
    # 처음에는 맨 마지막 까지 순환해야함 => 다음부터는 하나씩 줄여나감 : 마지막에 가장 큰 수 가 정렬되었기 때문
    for i in range(len(array)-1, 0, -1):
        # j는 마지막 인덱스 전(-1)까지만 돌면 됨 : j+1이 마지막에 위치하기 때문에
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
