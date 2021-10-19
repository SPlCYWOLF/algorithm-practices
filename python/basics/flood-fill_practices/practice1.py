dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


N = 4
G = [[0] * N for _ in range(N)]

G[0][2], G[1][3], G[3][1] = 1, 1, 1
Q = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            Q.append((i, j))

while Q:
    v = Q.pop(0)

    for i in range(4):
        nr = v[0] + dr[i]
        nc = v[1] + dc[i]

        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0:
            G[nr][nc] = G[v[0]][v[1]] + 1
            Q.append((nr, nc))
ans = max(max(G))
print(G)
print(ans)