# bfs - 인접 리스트 구현

def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if v not in visited:
            visited.append(v)
            for w in G[v]:
                if w not in visited:
                    Q.append(w)
    return ' -> '.join(map(str, visited))
    

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[] for _ in range(V+1)]

for i in range(len(temp)//2):
    p = temp[i*2]
    c = temp[i*2+1]
    G[p].append(c)

visited = []
print(bfs(1))