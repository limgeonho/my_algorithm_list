'''
무방향 그래프
인접 행렬
7 8 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

7 8
1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
'''


def bfs_3(s, V):
    q = [0] * V
    front = -1
    rear = -1
    visited = [0] * (V+1)       # visited 생성
    rear += 1                   # 시작점 인큐
    q[rear] = s
    visited[s] = 1              # 시작점 visited
    while front != rear:        # 큐가 비어있지 않으면
        front += 1              # 디큐해서 t에 저장
        t = q[front]
        print(t, end=' ')
        for i in range(1, V+1):  # t에 인접하고 미방문인 모든 i에 대해
            if board[t][i] == 1 and visited[i] == 0:
                rear += 1       # 인큐 i
                q[rear] = i
                visited[i] = visited[t] + 1  # i방문표시


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

bfs_3(1, V)
