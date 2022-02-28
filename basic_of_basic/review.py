n = int(input())
array = list(map(int, input().split()))

visited = [False] * len(array)
res = [0] * n

def perm(L):
    if L == n:
        print(res)
        return
    
    for i in range(len(array)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = array[i]
        perm(L+1)
        visited[i] = False

perm(0)