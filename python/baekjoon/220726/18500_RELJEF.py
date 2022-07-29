from collections import deque
import sys
sys.stdin = open('input.txt')


#   우  하  좌  상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


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
    chunks = []                                 # 미네랄 뭉치 저장 리스트
    Q = deque()
    Q.append((r, c))

    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if nr == R+1:                       # 바닥에 연결되어있다 = 공중에 떠있지 않은 미네랄
                return 0                        # 고로 bfs 종료

            if cave[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                chunks.append((nr, nc))
                Q.append((nr, nc))

    drop = 9999999999
    for chunk in chunks:        # 떨어질 최소 높이 구하기
        r, c = chunk
        d = 0
        if cave[r+1][c] == 1:
            continue
        while d < drop and cave[r+1][c] != 2:
            if cave[r+1][c] == 1 and (r+1, c) not in chunks:
                break
            r += 1
            d += 1
        drop = d

    for chunk in chunks:        # 떨어진 미네랄 위치 반영
        r, c = chunk
        cave[r][c] = 0
    for chunk in chunks:        # 중복 최신화 방지 위해 이전 위치 삭제 후 새로운 위치 입력
        r, c = chunk
        cave[r + drop][c] = 1


R, C = map(int, input().split())
cave = [[2]*(C+2)] + [[2] + list(map(toNum, input())) + [2] for _ in range(R)] + [[2]*(C+2)]
throws = int(input())
throw_h = list(map(int, input().split()))
# for i in range(1, R+1):
#     print(*cave[i][1:C+1])


for i in range(throws):
    r = R - throw_h[i] + 1      # 동굴 설정에 맞춰서 상하 반전
    if i % 2:                   # 우측에서 좌측으로 막대기 이동
        for j in range(C, 0, -1):
            if cave[r][j] == 1:         # 미네랄이 있으면
                cave[r][j] = 0          # 부시고
                for k in range(4):      # 4방향 붙어있던 미네랄 유무 확인
                    nr, nc = r + dr[k], j + dc[k]
                    if cave[nr][nc] == 1:
                        bfs(nr, nc)
                break               # 한번 던진 막대기가 미네랄에 막히면 스톱

    else:                       # 좌측에서 우측으로 막대기 이동
        for j in range(1, C+1):
            if cave[r][j] == 1:         # 미네랄이 있으면
                cave[r][j] = 0          # 부시고
                for k in range(4):      # 4방향 붙어있던 미네랄 유무 확인
                    nr, nc = r + dr[k], j + dc[k]
                    if cave[nr][nc] == 1:
                        bfs(nr, nc)
                break               # 한번 던진 막대기가 미네랄에 맞았으니 스톱

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