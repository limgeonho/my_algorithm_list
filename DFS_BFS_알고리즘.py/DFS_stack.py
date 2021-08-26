# dfs 탐색 알고리즘(깊이 우선 탐색)
# stack을 이용(DFS_stack)
# stack는 방문할 곳을 저장 => stack이 빌때까지 계속해서 탐색 => bfs와 비슷
# visited는 이미 지나온 곳을 기록
# dfs탐색은 시작점으로 부터 인접한 곳의 마지막 노드까지 탐색한 후에 다시 거꾸로 돌아오면서 나머지들을 탐색한다
# 그래프의 연결관계는 연결리스트 or 인접행렬

# 참고로, 2차원리스트의 길찾기 문제경우 visited를 만들지 않고 지나온 길을 1로 표시하면 원하는 방향으로 나아갈 수 있음
# => 하지만 재귀가 끝나고 나서는 다시 0으로 돌려놔야 다시 갈 수 있는 다른 방향으로 탐색가능

def dfs_stack(V, E, graph, S, G):
    # [0, 1 => False, 2 => False, 3 => False... ]
    visited = [False for _ in range(V+1)]
    stack = [S]

    while stack:
        current = stack.pop()
        # 방문하지 않았다면,
        if not visited[current]:
            visited[current] = True
            stack += graph[current]

    return visited[G]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    dfs_stack(V, E, graph, S, G)
