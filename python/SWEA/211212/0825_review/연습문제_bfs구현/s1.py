# 인접행렬 bfs 구현


def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print('{}정점에 방문'.format(v))
            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    Q.append(w)



import sys
sys.stdin = open('input.txt')

V,E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0] * (V+1) for _ in range(V+1)]

for i in range(len(temp)//2):
    p = temp[i*2]
    c = temp[i*2+1]
    G[p][c] = 1
    G[c][p] = 1

visited = [0] * (V+1)

bfs(1)