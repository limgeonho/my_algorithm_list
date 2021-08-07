# 플로이드_와샬 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단거리를 구하는 알고리즘
# 시간복잡도가 O(N**3)이기 때문에 N이 1000만 넘어도 1억이 넘어간다 => 많은 연산이 불가능...

INF = int(1e9)

n = int(input())
m = int(input())

# 초기값을 INF로 전부 설정한다.
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신까지의 거리는 전부 0으로 설정
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선에 대한 정보 입력(인접행렬)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 플로이드-와샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b])
