# 프림 알고리즘(크루스칼과 비슷)
# 크루스칼 알고리즘과 같은 목적으로 MST를 확인하는데 주 목적이 있다.
# 크루스칼은 간선의 가중치를 오름차순으로 정렬한 후 선택하는 반면에
# 프림알고리즘은 한 정점을 선택하고 이어지는 정점들 중 간선이 가장 작은 것을 선택해 나간다.
# 간선이 많은 경우에는 크루스칼보다 프림이 더 유리하다
# 구현하는 과정은 다익스트라와 비슷함

# 일반적인 prim
# O(ElogE)
# ================================================================================

from heapdict import heapdict
from collections import defaultdict
from heapq import *


def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
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
