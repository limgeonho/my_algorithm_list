# n = int(input())
# array = list(map(int, input().split()))
#
# visited = [False] * len(array)
# res = [0] * n

# def perm(L):
#     if L == n:
#         print(res)
#         return
#
#     for i in range(len(array)):
#         if visited[i]:
#             continue
#         visited[i] = True
#         res[L] = array[i]
#         perm(L+1)
#         visited[i] = False
#
# perm(0)
#
#
# def comb(L, start):
#     if L == n:
#         print(res)
#         return
#     for i in range(start, len(array)):
#         res[L] = array[i]
#         comb(L+1, i+1)
#
# comb(0, 0)

# def perm_with(L):
#     if L == n:
#         print(res)
#         return
#     for i in range(len(array)):
#         res[L] = array[i]
#         perm_with(L+1)
#
# perm_with(0)

# def subset(L, ss):
#     if L == n:
#         if not ss:
#             return
#         print(ss)
#         return
#     subset(L+1, ss + [array[L]])
#     subset(L+1, ss)
#
# subset(0, [])
#
#
# def next_perm(array):
#     i = len(array)-1
#     while i > 0 and array[i-1] >= array[i]:
#         i -= 1
#
#     if i < 0:
#         return False
#
#     j = len(array) - 1
#     while array[i-1] >= array[j]:
#         j -= 1
#
#     array[i-1], array[j] = array[j], array[i-1]
#
#     j = len(array) - 1
#     while i < j:
#         array[i], array[j] = array[j], array[i]
#         i += 1
#         j -= 1
#
#     return True

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v+1)
#
# for i in range(1, v+1):
#     parent[i] = i
#
# # for _ in range(e):
# #     a, b = map(int, input().split())
# #     union_parent(parent, a, b)
#
#
# edges = []
# result = 0
# cnt = 0
#
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a , b))
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         cnt += 1

# text = 'dasdsadvfdg'
# target = 'fds'
#
# idx = -1
#
# while True:
#     idx = text.find(target)
#     if idx == -1:
#         break
#
#     print(idx, end=' ')
#
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return None

# import math
# def is_prime(x):
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#         else:
#             return True

# n = 1000
# array = [True for i in range(n+1)]
#
#
# for i in range(2, int(n**0.5)+1):
#     if array[i]:
#         j = 2
#         while i * j <= n:
#             array[i*j] = False
#             j += 1
#
# for i in range(2, n+1):
#     if array[i]:
#         print(i, end=' ')

# def change(n, notation):
#     tmp = ''
#     while n > 0:
#         n, mod = divmod(n, notation)
#         tmp += str(mod)
#
#     return tmp[::-1]
#
# print(change(11, 2))

# def change(n, notation):
#     tmp = ''
#     while n > 0:
#         n, mod = divmod(n, notation)
#         tmp += str(mod)
#
#     return tmp[::-1]
# from collections import Counter
# text = 'sdfsafsagsadfsafasf'
# # answer = {}
# # for s in text:
# #     answer[s] = answer.get(s, 0) + 1
# #
# # print(answer)
#
# counter = Counter(text)
# print(dict(counter))

# import heapq
#
# def heap(iterable):
#     h = []
#     result = []
#     for value in iterable:
#         heapq.heappush(h, -value)
#
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h))
#
#     return result
#
# answer = heap([1, 4, 6, 2, 6,7,8, 342, 54])
# print(answer)

# import math
# a = 21
# b = 14
# print((a*b)// math.gcd(21, 14))

# n, limit = map(int, input().split())
#
# dy = [0] * (limit+1)
# #
# # for i in range(n):
# #     weight, value = map(int, input().split())
# #
# #     for j in range(limit, weight-1, -1):
# #         dy[j] = max(dy[j], dy[j-weight] + value)
# #
# # print(dy[limit])
#
# for i in range(n):
#     weight, value = map(int, input().split())
#
#     for j in range(weight, limit+1):
#         dy[j] = max(dy[j], dy[j-weight] + value)
#
# print(dy[limit])

from bisect import bisect_left
# array = [3, 1, 2, 4, 8, 6, 7]
# n = len(array)
# dp = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j]+1)
#
# result = max(dp)
# print(result)
#
# dp = [array[0]]
# for i in range(1, n):
#     if dp[-1] < array[i]:
#         dp.append(array[i])
#     else:
#         dp[bisect_left(dp, array[i])] = array[i]
# result = len(dp)
#
# print(result)

# dp =[1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j]+1)
#
# order = max(dp)
# print(array)
# print(dp)
# answer = []
# for i in range(n-1, -1, -1):
#     if dp[i] == order:
#         answer.append(array[i])
#         order -= 1
# print(answer[::-1])

# import heapq
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# distance = [999999] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = i[1] + dist
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(start)

# INF = int(999999999)
#
# n = int(input())
# m = int(input())
#
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#
# for k in range(1, n+1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# def matrix(arr1, arr2):
#     row = len(arr1)
#     col = len(arr2[0])
#
#     answer = [[0] * col for _ in range(row)]
#
#     for i in range(row):
#         for j in range(col):
#             for k in range(arr1[0]):
#                 answer[i][j] += arr1[i][k] * arr2[k][j]
#
#     return answer
#
# answer = [k[::-1]for _ in zip(*arr)]

# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# def rotate(a):
#     row = len(a)
#     col = len(a[0])
#
#     changed = [[0]*row for _ in range(col)]
#
#     for r in range(row):
#         for c in range(col):
#             changed[c][row-1-r] = a[r][c]
#
#     return changed
#
# print(rotate(a))


# data = [1,3,5,4,2,58,4,2,3,8,1,2,3]
# n = len(data)
# m = 6
#
#
# cnt = 0
# interval = 0
# end = 0
#
# for start in range(n):
#     while interval < m and end < n:
#         interval += data[end]
#         end += 1
#
#     if interval == m:
#         cnt += 1
#
#     interval -= data[start]
#
# print(cnt)

