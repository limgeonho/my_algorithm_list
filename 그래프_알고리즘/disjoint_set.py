# 서로소 집합 알고리즘 + 사이클 판별
# 연결관계가 복잡한 집합을 같은 부모를 공유하는 집합끼리 묶을 수 있음
# 이를 통해 무방향그래프의 사이클을 판별할 수 있음(반드시 무방향!)
# 사이클 = 같은 부모를 공유하는 집합의 덩어리(하나로 연결되어 닫혀있음) = 특정정점에서 출발하면 해당 정점으로 돌아올 수 있는 것
# union(서로 다른 두 원소 합치기)과 find(부모 찾기)함수를 구현

# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 연결된 두 원소 중 작은 번호의 원소를 부모로 한다


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# v는 노드 e는 간선
v, e = map(int, input().split())
parent = [0] * (v+1)

# 처음에는 자기 자신을 부모로 설정
for i in range(1, v+1):
    parent[i] = i

# 서로소 집합
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 부모 테이블 출력
for i in range(1, v+1):
    print(parent[i], end=' ')

# 사이클 판별=================================
# cycle = False

# for _ in range(e):
#     a, b = map(int, input().split())
#     # 사이클이 발생
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle = True
#         break
#     # 사이클이 발생하지 않았다면 계속해서 union(합집합) 수행
#     else:
#         union_parent(parent, a, b)
