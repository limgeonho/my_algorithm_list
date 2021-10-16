# 프림 알고리즘(크루스칼과 비슷)
# 크루스칼 알고리즘과 같은 목적으로 MST를 확인하는데 주 목적이 있다.
# 크루스칼은 간선의 가중치를 오름차순으로 정렬한 후 선택하는 반면에
# 프림알고리즘은 한 정점을 선택하고 이어지는 정점들 중 간선이 가장 작은 것을 선택해 나간다.
# 간선이 많은 경우에는 크루스칼보다 프림이 더 유리하다
# 구현하는 과정은 다익스트라와 비슷함

# 일반적인 prim
# O(ElogE)
# ================================================================================

import heapq
from heapdict import heapdict
from collections import defaultdict
from heapq import *


def prim(start_node, edges):
    # 최소신장트리를 저장할 리스트
    mst = list()
    # 인접간선리스트 => defaultdict을 통해 default를 list()로 설정
    adjacent_edges = defaultdict(list)
    # 간선정보를 입력
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    # 시작노드를 set()에 넣어줌 => 싸이클 여부 판별을 위해
    connected_nodes = set(start_node)
    # 시작노드의 간선리스트를 후보리스트에 등록
    candidate_edge_list = adjacent_edges[start_node]
    # 후보리스트를 heapq구조화
    heapify(candidate_edge_list)

    # 후보리스트를 순회
    while candidate_edge_list:
        # 후보리스트 중 가장 가중치가 작은 간선을 pop
        weight, n1, n2 = heappop(candidate_edge_list)
        # 연결 될 노드가 싸이클에 포함되는지 여부 판단
        if n2 not in connected_nodes:
            # 포함되지 X => set()에 추가
            connected_nodes.add(n2)
            # 해당 노드정보를 MST에 추가
            mst.append((weight, n1, n2))

            # 연결 확정된 다음 노드의 간선리스트들을 후보리스트에 heappush
            for edge in adjacent_edges[n2]:
                # 연결가능한 간선리스트들 중 n2가 이미 connected_nodes에 있다면 => 싸이클이 존재 => 후보리스트에 넣지 X
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst


# 개선된 prim
# O(ElogV)
# ===============================================================================
def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key
        for adjacent, weight in mygraph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node
    return mst, total_weight


# ===============================================================================
# from collections import defaultdict

# list_dict1 = defaultdict(list)
# print(list_dict1['key1']) => []

# list_dict2 = defaultdict(int)
# print(list_dict2['key2']) => 0

# ===============================================================================


def prim():

    q = []
    # (0, 0) => (가중치, 시작점)
    heapq.heappush(q, (0, 0))
    answer = 0

    while q:
        w, v = heapq.heappop(q)
        # 방문한지 확인(= MST에 포함되어 있는지 확인)
        if not visited[v]:
            answer += w
            visited[v] = 1

            for idx, weight in adj[v]:
                if not visited[idx]:
                    heapq.heappush(q, (weight, idx))


v, e = map(int, input().split())

adj = [[] for _ in range(v+1)]

# MST에 포함되었는지 visisted로 확인 why? => heapq에서는 작은 순서대로 나옴
visited = [0] * (v+1)


for i in range(e):
    n1, n2, w = map(int, input().split())
    # 양방향 그래프
    adj[n1].append((n2, w))
    adj[n2].append((n1, w))

prim()
