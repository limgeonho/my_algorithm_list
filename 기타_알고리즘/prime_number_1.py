# 소수 구하기

import math


def is_prime_number(x):
    # 2부터 x-1까지가 아니라 제곱근까지만 확인하는 것이 핵심
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        else:
            return True
