from collections import Counter
# Counter
# iterable의 객체 중에서 해당 객체 내의 원소가 몇 번씩 등장하는지 알려주는 라이브러리
# 리스트나 문자열에서 같은 내용이 몇 번씩 나왔는지 구해야하는 문제에서 유용하게 사용됨
# 반환되는 type는 counter이기 때문에 dict()로 변환해주면 편리하게 사용가능

counter = Counter(['red', 'blue', 'green', 'blue', 'blue', 'red'])
print(dict(counter))
# {'red': 2, 'blue': 3, 'green': 1}

# ==============================================================================

strings = Counter('abcabcdddabcfdsfds')
print(dict(strings))
# {'a': 3, 'b': 3, 'c': 3, 'd': 5, 'f': 2, 's': 2}

# ==============================================================================

strings_not_use_counter = 'abcabcdddabcfdsfds'
answer = {}
for s in strings_not_use_counter:
    answer[s] = answer.get(s, 0) + 1
print(answer)
# {'a': 3, 'b': 3, 'c': 3, 'd': 5, 'f': 2, 's': 2}
