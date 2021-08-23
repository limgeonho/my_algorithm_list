# 부분집합 구하기(DFS 사용)
# 노드를 하나씩 내려갈 때마다 선택여부를 0, 1로 표시한다. => 재귀
# 마지막노드까지 내려가면 check리스트를 확인하여 선택된 인자의 index만 출력 후 다시 뒤로 돌아가서 순회

def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)


n = 3
check = [0] * (n+1)
DFS(1)
