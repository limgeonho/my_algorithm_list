from bisect import bisect_left, bisect_right
# 이진탐색 라이브러리(bisect)활용하기
# from bisect import bisect_left, bisect_right
# bisect_left(array, x) => array안에 x가 삽입되어야할 위치를 반환하고 이미 x가 존재할 경우 x의 왼쪽 위치를 반환한다.
array = [1, 3, 5, 7, 9]
x = 4

print(bisect_left(array, x))
# print(bisect_right(array, x))
