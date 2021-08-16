# 위상정렬
# 뱡향그래프의 모든 노드를 방향성에 거스르지 않고 순서대로 나열하는 것
# 진입차수가 0인 노드부터 queue에 넣고 돌린다.
# queue에서 빠져나간 순서 = 위상정렬 결과

from collections import deque

v, e = map(int, input().split())

# 모든 노드에 대해서 진입차수 0으로 초기화
indegree = [0] * (v+1)

# 연결리스트
graph = [[]for _ in range(v+1)]

# 초기 설정
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # (a -> b)이기 때문에 b의 진입차수를 1증가
    indegree[b] += 1


# 위상 정렬
def topology_sort():
    result = []
    q = deque()

    # 전체 노드의 노드 중에서 진입차수가 0인 노드를 q에 append
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # q에서 뽑은 노드와 연결되어 있는 노드들의 진입차수를 -1 하고 그 중 진입차수가 0인 노드를 q에 append
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()
