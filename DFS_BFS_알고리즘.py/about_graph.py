"""
Graph

Vertex(Node): 꼭지점
Edge: 간선

Undirected Graph: 간선에 방향이 없음(양방향 이동 가능)
Directed Graph: 간선에 방향이 있음(단방향 이동만 가능)

V: 6개
E: 5개
1 4
1 3
2 3
2 5
4 6

Start 1
Goal 6
for _ in range(E):
"""
V = 6
E = 5

S = 1
G = 6

# 1. Dictionary
g = {
    'A': ['D', 'C'],
    'B': ['C', 'E'],
    'C': [],
    'D': ['F'],
    'E': [],
    'F': []
}

# 2. Adjacency List
g = [[],  # 0
     [4, 3],  # 1
     [3, 5],  # 2
     [],  # 3
     [6],  # 4
     [],  # 5
     [],  # 6
     ]

# 3. Adj Matrix
[
    [F, T, F, F, F],
    [F, F, F, T, F],
    [F, T, F, F, F],
]
