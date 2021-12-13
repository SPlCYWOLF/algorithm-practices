def bfs(v):
    not_visited.append(v)
    while not_visited:
        v = not_visited.pop(0)
        if v not in visited:
            visited.append(v)
            not_visited.extend(G[v])
    return ' -> '.join(map(str, visited))


import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = {}

for i in range(1, V+1):
    G[i] = []

for i in range(0, len(temp), 2):
    G[temp[i]].append(temp[i+1])
    print(G)
    G[temp[i+1]].append(temp[i])
    print(G)

visited = []
not_visited = []
print(bfs(1))