# 다익스트라 알고리즘
# 한 정점에서 다른 정점으로 갈 수 있는 최단 거리
# heapq 사용하기
#


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n은 노드, m은 간선
n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# start는 시작노드


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i[1]은 간선의 가중치
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
