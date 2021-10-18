```python
'''
flood-fill 문제
배열에서 숫자가 상하좌우로 펴져나가는데, 퍼져나갈때 마다 숫자가 1씩 증가한다.
배열을 꽉 채우게 됬을때, 가장 큰 숫자를 반환하라.
'''
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def finder(r, c):
    Q = [(r, c)]

    while Q:
        v = Q.pop(0)
        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]

            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 0:
                Q.append((nr, nc))
                maze[nr][nc] = maze[v[0]][v[1]] + 1


N, M = 3, 4
maze = [[0] * M for _ in range(N)]
maze[1][1] = 1
finder(1, 1)
print(max(max(maze)))       # 배열에서 가장 큰 값 == 정답
```

