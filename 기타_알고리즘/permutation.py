# 순열 알고리즘
# 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것(중복 X)

# [1, 2, 3] 의 순열
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
