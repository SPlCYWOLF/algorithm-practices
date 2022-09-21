from collections import deque
import sys
sys.stdin = open('input.txt')

# BFS활용하여 목적지까지의 이동횟수 및 도착가능 여부 확인

# 상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


N, M = map(int, input().split())
field = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
ans = -1

visited = [[0] * (M+2)] + [[0] + [0] * M + [0] for _ in range(N)] + [[0] * (M+2)]

Q = deque()
Q.append((1, 1, False, 0)) # 현재위치, 현재방향, 냄새여부, 이동횟수
visited[1][1] = 1
found = False   # 정답 찾을 시 종료 플래그 변수
while Q:

    r, c, smells, cnt = Q.popleft()

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if field[nr][nc] and not visited[nr][nc]:

            if field[nr][nc] == 2:
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    found = True
                    break

                Q.append((nr, nc, True, cnt+1))

            elif field[nr][nc] == 3:
                if smells:
                    visited[nr][nc] = 1
                    if nr == N and nc == M:
                        ans = cnt + 1
                        found = True
                        break

                    Q.append((nr, nc, smells, cnt+1))

            elif field[nr][nc] == 4:
                if nr == N and nc == M:
                    ans = cnt + 1
                    found = True
                    break

                moved = 1
                while field[nr][nc] == 4:
                    visited[nr][nc] = 1
                    nr, nc = nr + dr[k], nc + dc[k]
                    moved += 1

                if field[nr][nc] == 2:
                    if nr == N and nc == M:
                        ans = cnt + moved
                        found = True
                        break

                    Q.append((nr, nc, True, cnt+moved))

                elif field[nr][nc] == 3:
                    nr, nc = nr - dr[k], nc - dc[k]
                    Q.append((nr, nc, False, cnt + moved - 1))

                elif field[nr][nc] == 1:
                    if nr == N and nc == M:
                        ans = cnt + moved
                        found = True
                        break

                    Q.append((nr, nc, False, cnt+moved))

            else:
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    found = True
                    break

                Q.append((nr, nc, smells, cnt+1))

    if found:
        break

print(ans)

