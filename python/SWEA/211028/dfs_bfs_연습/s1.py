import sys
sys.stdin = open('input.txt')


def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if v not in visited:
            visited.append(v)
            for i in G:
                if i[0] == v and i[1] not in visited:
                    Q.append(i[1])

    return visited


def dfs(v):
    visited.append(v)
    for i in range(E):
        if G[i][0] == v and G[i][1] not in visited:
            dfs(G[i][1])
    return visited


# for tc in range(1, int(input())+1):

N, E, start = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(E)]
visited = []
# print(G)

print('dfs: {}'.format(dfs(start)))
visited = []
print('bfs: {}'.format(bfs(start)))