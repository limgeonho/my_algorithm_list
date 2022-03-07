# n = int(input())
# arr = list(map(int, input().split()))
# visited = [False] * len(arr)
# res = [0] * n

# def perm(L):
#     if L == n:
#         print(*res)
#         return
#     for i in range(len(arr)):
#         if visited[i]:
#             continue
#         visited[i] = True
#         res[L] = arr[i]
#         perm(L+1)
#         visited[i] = False
#
# # perm(0)
#
# def comb(L, start):
#     if L == n:
#         print(*res)
#         return
#     for i in range(start, len(arr)):
#         res[L] = arr[i]
#         comb(L+1, i+1)
#
# # comb(0, 0)
#
# def perm_with(L):
#     if L == n:
#         print(*res)
#         return
#     for i in range(len(arr)):
#         res[L] = arr[i]
#         perm_with(L+1)
#
# perm_with(0)

# arr = list(int, input().split())

# def next_perm(arr):
#     i = len(arr)-1
#     while i > 0 and arr[i-1] >= arr[i]:
#         i -= 1
#     if i < 0:
#         return False
#
#     j = len(arr) - 1
#     while arr[i-1] >= arr[j]:
#         j -= 1
#
#     arr[i-1], arr[j] = arr[j], arr[i-1]
#     j = len(arr) - 1
#
#     while i < j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j -= 1
#     return True


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges = []
result = 0
cnt = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1
        result += cost

if cnt == v-1:
    print("MST")
else:
    print(-1)

def binart_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1

    return None


n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(n**0.5)+1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')

def change(x, notation):
    tmp = ''
    while x > 0:
        x, mod = divmod(x, notation)
        tmp += str(mod)

    return tmp[::-1]

n, limit = map(int, input().split())
dy = [0] * (limit+1)

for i in range(n):
    weight, value = map(int, input().split())

    for j in range(limit, weight-1, -1):
        dy[j] = max(dy[j], dy[j-weight] + value)

    ############################################

    for j in range(weight, limit+1):
        dy[j] = max(dy[j], dy[j-weight] + value)


# changed = [k[::-1] for _ in zip(*arr)]

import heapq
n, m = map(int, input().split())
start = int(input())
graph = [[]for _ in range(n+1)]
distance = [999999] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))