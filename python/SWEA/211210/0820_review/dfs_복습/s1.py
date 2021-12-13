# 인접행렬

def dfs(v):
    for j in range(1, V+1):
        if G[v][j] == 1:
           visited[j] = 1
    return visited 


import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    p = temp[i*2]
    c = temp[i*2+1]
    G[p][c] = 1
    G[c][p] = 1
print(G)


for i in range(1, V+1):
    visited = [0] * (V+1)
    print('방문정점: {}, 인접정점: {}'.format(i, dfs(i)))
