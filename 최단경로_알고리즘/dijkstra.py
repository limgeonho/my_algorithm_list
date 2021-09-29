# 다익스트라 알고리즘
# 한 정점에서 다른 정점으로 갈 수 있는 최단 거리
# heapq 사용하기
# 힙에 push할때 가중치와 노드번호를 반대로 넣어준다 = 그래야 가중치를 기준으로 오름차순 정렬됨


import heapq
import sys
from typing_extensions import IntVar
input = sys.stdin.readline
INF = sys.maxsize

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
        # dist == 지금까지 now에 오는데 걸리는 비용(거리)
        dist, now = heapq.heappop(q)
        # distance[now] < dist를 처리하는 이유 : heapq를 사용하기 때문에 같은 노드로 가야하는 경우가 여러개 존재할 수 있지만 우선순위에 밀려서 나오지 못한 상황이 존재한다
        # 따라서, heapq에 남아있는(우선순위에서 밀린)노드들을 처리하는 과정 == 이미 distance에 더 작은 값이 저장되어 있다면 continue
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


# ==================================================================
# 다익스트라 경로구하기

# sys.maxsize로 INF초기화 하기..
INF = sys.maxsize

n = int(input())  # 노드 수
m = int(input())  # 간선 수
graph = [[]for i in range(n+1)]  # 연결리스트
distance = [INF] * (n+1)  # 최단 경로 리스트

#################################################################
# 경로추적 리스트
trace = [0] * (n+1)
#################################################################

# 간선 정보 입력(연결리스트)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발점, 도착점
start, end = map(int, input().split())


# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                #################################################################
                # 추가 trace[다음 노드] = 현재 노드
                trace[i[0]] = now
                #################################################################
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

#################################################################
# 추가(맥락은 order 역추적과 같음)
path = [end]  # path : 경로를 담을 리스트
prev_node = trace[end]  # 추적리스트에 end값부터 넣어줌(prev_node == 이전 노드))
while True:
    if prev_node == 0:  # prev_node(이전 노드)가 0(더 이상 갈 곳이 없음)이면 끝
        break
    path.append(prev_node)  # 경로 리스트에 이전 노드를 추가
    prev_node = trace[prev_node]  # 다시 추적리스트에 prev_node 세팅
#################################################################

print(distance[end])
print(len(path))
print(*path[::-1])  # path에는 마지막 순서부터 들어갔기 때문에 거꾸로 출력
