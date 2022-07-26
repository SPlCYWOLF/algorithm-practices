from collections import deque
import sys
sys.stdin = open('input.txt')


#   우  하  좌  상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# 처음 진입 확인용
#     우  좌  상
idr = (0, 0, -1)
idc = (1, -1, 0)

def take_second(elem):
    return elem[1]
def take_first(elem):
    return elem[0]
def toStr(n):
    if n == 0:
        return '.'
    else:
        return 'x'
def toNum(n):
    if n == '.':
        return 0
    else:
        return 1

def bfs(r, c):
    visited = [[0] * (C+2) for _ in range(R+2)]
    chunks = []
    Q = deque()
    Q.append((r, c))

    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if nr == R:                         # 공중에 떠있지 않은 미네랄
                return 0

            if cave[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                chunks.append((nr, nc))
                Q.append((nr, nc))

    chunks = sorted(chunks, key=take_first, reverse=True)
    chunks = sorted(chunks, key=take_second, reverse=True)
    n = len(chunks)
    min_h_list = []
    temp = 0
    for i in range(n):          # col 별로 최소 높이 저장
        r, c = chunks[i]
        if c != temp:
            temp = c
            min_h_list.append((r, c))

    drop = 9999999999
    for min_h in min_h_list:    # 모든 col의 최소 값 중 다음 미네랄까지의 최소 높이 저장
        r, c = min_h
        d = 0
        while cave[r+1][c] == 0:
            r += 1
            d += 1
        drop = min(drop, d)

    for chunk in chunks:        # 떨어진 미네랄 위치 반영
        r, c = chunk
        cave[r][c] = 0
        cave[r+drop][c] = 1


R, C = map(int, input().split())
cave = [[2]*(C+2)] + [[2] + list(map(toNum, input())) + [2] for _ in range(R)] + [[2]*(C+2)]
throws = int(input())
throw_h = list(map(int, input().split()))
for i in range(1, R+1):
    print(*cave[i][1:C+1])
for i in range(R+2):
    print(*cave[i])

for i in range(throws):
    r = R - throw_h[i] + 1
    if i % 2:
        # print(f'to left: {throw_h[i]}')
        for j in range(C, 0, -1):
            if cave[r][j]:     # 미네랄이 있고, 좌 or 우 or 위에 미네랄이 있으면 bfs 시작
                cave[r][j] = 0
                for k in range(3):
                    nr, nc = r + idr[k], j + idc[k]
                    if cave[nr][nc] == 1:
                        bfs(nr, nc)
                break

    else:
        # print(f'to right: {throw_h[i]}')
        for j in range(1, C+1):
            if cave[r][j]:     # 미네랄이 있고, 좌 or 우 or 위에 미네랄이 있으면 bfs 시작
                cave[r][j] = 0
                for k in range(3):
                    nr, nc = r + idr[k], j + idc[k]
                    if cave[nr][nc] == 1:
                        bfs(nr, nc)
                break

print()
for i in range(1, R+1):
    print(*cave[i][1:C+1])
print()
for i in range(1, R+1):
    for j in range(1, C+1):
        if cave[i][j] == 1:
            print('x', end='')
        else:
            print('.', end='')
    if i == R:
        break
    print()
