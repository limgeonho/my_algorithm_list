# 프림 알고리즘(크루스칼과 비슷)
# 크루스칼 알고리즘과 같은 목적으로 MST를 확인하는데 주 목적이 있다.
# 크루스칼은 간선의 가중치를 오름차순으로 정렬한 후 선택하는 반면에
# 프림알고리즘은 한 정점을 선택하고 이어지는 정점들 중 간선이 가장 작은 것을 선택해 나간다.
# 간선이 많은 경우에는 크루스칼보다 프림이 더 유리하다
# 구현하는 과정은 다익스트라와 비슷함

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline


n, m = map(int, input().split())    # n은 노드 수, m은 간선 수
graph = defaultdict(list)   # 빈 그래프 생성
visited = [0] * (n+1)   # 노드 방문 확인 리스트

# 무방향 그래프
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, a, b])
    graph[b].append([cost, b, a])


# prim_algorithm
def prim(graph, start):
    visited[start] = 1    # 첫 노드 방문 체크 => 1
    candidate = graph[start]    # 인접 간선 정보 추출
    heapq.heapify(candidate)    # heapq 생성
    mst = []    # 최소 신장 트리
    result = 0    # 전체 가중치

    while candidate:
        cost, a, b = heapq.heappop(candidate)   # 가중치가 가장 적은 간선 정보 추출
        if visited(b) == 0:   # 방문하지 않았다면
            visited[b] = 1    # 방문 갱신
            mst.append((a, b))    # mst에 추가
            result += cost    # 가중치 누적

            for edge in graph[b]:   # 다음 인접 간선 탐색
                if visited[edge[2]] == 0:   # 방문한 노드가 아니라면
                    heapq.heappush(candidate, edge)
    return result


print(prim(graph, 1))
