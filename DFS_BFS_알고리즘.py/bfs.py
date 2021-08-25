'''
무방향 그래프
인접 행렬
7 8 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

7 8
1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
'''


def bfs_1(s, V):
    q = []                  # 큐 생성
    visited = [0] * (V+1)   # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시

    while q:                      # 큐가 비어있지 않으면(처리할 정점이 남아 있으면)
        now = q.pop(0)            # 디큐해서 t에 저장
        print(now, end=' ')       # t에 대한 처리
        for i in range(1, V+1):   # t에 인접이고 미방문인 모든 i에 대해
            if board[now][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1


def bfs_2(s, V):
    q = []                  # 큐 생성
    visited = [0] * (V+1)   # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시

    while q:                        # 큐가 비어있지 않으면(처리할 정점이 남아 있으면)
        now = q.pop(0)              # 디큐해서 now에 저장
        print(now, end=' ')         # t에 대한 처리
        for i in board_list[now]:   # t에 인접이고 미방문인 모든 i에 대해
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))
board = [[0] * (V+1) for _ in range(V+1)]   # 인접행렬
board_list = [[] for _ in range(V+1)]       # 인접리스트

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    board[n1][n2] = 1
    board[n2][n1] = 1  # 방향이 없는 그래프(인접행렬)

    board_list[n1].append(n2)
    board_list[n2].append(n1)   # 방향이 없는 그래프(인접리스트)

bfs_1(1, V)
bfs_2(1, V)
