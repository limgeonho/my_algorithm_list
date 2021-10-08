# 진수 변환 방법

# n진수 -> 10 진수
# int(<해당 진수로 만들어진 수>, 해당진수) -> 10진수 값으로 변환된다.
print(int('111', 2))

# 10진수 -> n진수


def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


print(solution(45, 3))

print(solution(11, 2))



def change(n, notation):
    tmp = ''
    while n > 0:
        n, mod = divmod(n, notation)
        tmp += str(mod)

    return tmp[::-1]