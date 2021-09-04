# 다익스트라 알고리즘
# 한 정점에서 다른 정점으로 갈 수 있는 최단 거리
# heapq 사용하기
# 힙에 push할때 가중치와 노드번호를 반대로 넣어준다 = 그래야 가중치를 기준으로 오름차순 정렬됨


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n은 노드, m은 간선
n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n+1)]
distance = [INF] * (n+1)

# 간선 정보 입력(연결리스트)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# start는 시작노드
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i[1]은 간선의 가중치
            cost = dist + i[1]
            # 중요한 점 : 지금까지 거리의 cost를 가지고 있는 distance값과 비교했을때 탐색하려는 cost가 작다면 업데이트하고 -> heapq에 heappush한다!!
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
