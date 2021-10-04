# 크루스칼 알고리즘
# 최소신장트리(MST = minimum spanning tree)를 찾는 알고리즘
# 조건1 : 간선의 개수 = 노드의 개수 - 1
# 조건2 : 신장트리의 간선의 총합은 가능한 경우의 수 중 가장 작아야 함
# 활용 : 도로망, 네트워크망, 통신망 등...
# 그리디 알고리즘 중 하나임
# 간선에 대해 오름차순 정렬을 하고 사이클 발생시에는 포함X
# disjoint_set을 이용하기 때문에 상당히 비슷

# ====================================== disjoint_set ======================================
# 부모 찾기(path-compression)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 연결된 두 원소 중 작은 번호의 원소를 부모로 한다(union-by-rank)
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

# ==========================================================================================

# 간선들을 저장할 edge리스트와 최종 비용 result 선언
edges = []
result = 0

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해 cost부터 append
    edges.append((cost, a, b))

edges.sort()
# 만들어진 결과물이 MST인지 확인!!!
cnt = 0

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        cnt += 1

# MST를 충족하는 최소 비용
print(result)


# MST 여부 확인 => MST의 경로 개수 == 노드 - 1
if cnt == v-1:
    print('MST 맞음')
else:
    print('MST 아님')
