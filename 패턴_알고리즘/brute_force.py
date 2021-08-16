# brute_force(패턴을 찾는 알고리즘)

# 일반적인 문자열 찾기 알고리즘

def find_string(parent, pattern):

    parent_length = len(parent)
    pattern_length = len(pattern)

    for i in range(parent_length - pattern_length + 1):
        finded = True
        for j in range(pattern_length):
            if parent[i + j] != pattern[j]:
                finded = False
                break
        if finded:
            return i
    return -1


print(find_string('hello world', 'llo'))


# =======================================================================
