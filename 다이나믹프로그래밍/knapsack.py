# 냅색알고리즘(가방문제...)
# 주어진 제한된 상황 속에서 최대한의 가치를 만들어내는 알고리즘
# 여러가지 물건들과 해당 물건들의 가치가 존재할 때 하나씩 입력받는다.
# 핵심은 한가지 물건을 선택했다고 가정하고 해당 물건의 가치를 추가한다.
# 같은 과정을 전체 물건을 적용하면서 최신화한다.

# n은 물건개수, limit는 최대로 들어갈 수 있는 값
n, limit = map(int, input().split())

# dy리스트의 인덱스 = 인덱스 만큼의 무게에서 갖는 최대한의 가치
dy = [0] * (limit+1)

for i in range(n):
    weight, value = map(int, input().split())
    # 선택한 물건의 가치를 포함하는 것을 적용한다고 가정하기 때문에 for문의 시작이 weight임
    # => 안그러면 음수 index
    for j in range(weight, limit+1):
        # weight를 포함했다고 가정하고 value를 추가한 상태에서 순환
        dy[j] = max(dy[j], dy[j-weight] + value)

print(dy[limit])
