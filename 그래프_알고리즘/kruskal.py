# 크루스칼 알고리즘
# 최소신장트리(MST = minimum spanning tree)를 찾는 알고리즘
# 조건1 : 간선의 개수 = 노드의 개수 - 1
# 조건2 : 신장트리의 간선의 총합은 가능한 경우의 수 중 가장 작아야 함
# 활용 : 도로망, 네트워크망, 통신망 등...
# 그리디 알고리즘 중 하나임
# 간선에 대해 오름차순 정렬을 하고 사이클 발생시에는 포함X
# disjoint_set을 이용하기 때문에 상당히 비슷

# ====================================== disjoint_set ======================================
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

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# MST를 충족하는 최소 비용
print(result)


# 두 번째 방법(path-compression, union-by-rank기법 활용)
# ==============================================================================

parent = dict()
rank = dict()


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst
