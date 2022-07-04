import sys
sys.stdin = open('input.txt')


def bfs(v):
    global cnt
    Q = [v]
    while Q:
        virus = Q.pop(0)
        if not visited[virus]:
            visited[virus] = 1
            Q += network[virus]
            cnt += 1


N = int(input())
E = int(input())
network = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for i in range(E):
    current, goal = map(int, input().split())
    network[current] += [goal]
    network[goal] += [current]

bfs(1)
print(cnt-1)