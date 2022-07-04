import sys
sys.stdin = open('input.txt')


def dfs(v):
    print(v, end=" ")
    for destination in graph[v]:
        if not visited[destination]:
            visited[destination] = 1
            dfs(destination)

def bfs(v):
    visited[v] = 1
    Q = graph[v]
    print(v, end=" ")

    while Q:
        destination = Q.pop(0)
        if not visited[destination]:
            visited[destination] = 1
            Q += graph[destination]
            print(destination, end=" ")


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    current, goal = map(int, input().split())
    graph[current] += [goal]
    graph[goal] += [current]
for nums in graph:
    nums.sort()

visited = [0] * (N+1)
visited[V] = 1
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)