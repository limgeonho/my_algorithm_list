# 패턴을 찾는 pythonic한 방법
# 1. in연산자 => True / False로 결과가 나옴
# 2. find() => 찾는 target이 위치하는 text의 시작 index값이 나옴(내부적으로 boyer-moore로 설계되어 있기 때문에 빠름)
# text.find(target, <시작위치>)

text = 'abcabcbabcbafkhsdalfkhsa'
target = 'ab'

# text내에서 처음으로 target가 나타나는 위치가 반환된다.
print(text.find(target))

# target가 존재하는 모든 위치를 탐색하는 방법
index = -1
while True:
    index = text.find(target, index+1)
    if index == -1:
        break
    print(index, end=' ')

print(dir(dict))
