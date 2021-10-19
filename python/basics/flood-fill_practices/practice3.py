dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

N, M = 4, 5

maze = [
    [0, 1, 1, 1, 'G'],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
Q = []
Q.append((0, 0))

while Q:
    v = Q.pop(0)
    for k in range(4):
        nr = v[0] + dr[k]
        nc = v[1] + dc[k]

        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == 'G':
                print('found goal at {}th step'.format(maze[v[0]][v[1]] + 1))

            if maze[nr][nc] == 0:

                Q.append((nr, nc))
                maze[nr][nc] = maze[v[0]][v[1]] + 1
print(maze)

