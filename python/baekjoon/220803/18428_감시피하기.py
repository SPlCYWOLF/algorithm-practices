import sys
sys.stdin = open('input.txt')

# 선생님의 숫자가 적음, 고로 선생님 기준으로 학생이 보이면 장애물 설치
# bfs 활용하여 각 선생님 기준으로 상우하좌 한칸씩 가려보며 3개의 장애물 설치가 완료되 때 마다
# 선생님 기준으로 loop 돌며 가려진 여부 확인
# 가려졌으면 YES, 아니면 NO 반환

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c):
    global obstacles, ans
    if obstacles == 0:
        # ans = "NO"
        return

    for l in range(4):
        nr, nc = r + dr[l], c + dc[l]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = 1

            if bokdo[nr][nc] == "S":
                obstacles = 0
                ans = "NO"
                return
            if bokdo[nr][nc] == "O":
                continue
            if bokdo[nr][nc] == "T":
                dfs(nr, nc)
                continue

            for k in range(1, N):
                nnr, nnc = nr + (dr[l] * k), nc + (dc[l] * k)

                if 0 <= nnr < N and 0 <= nnc < N and not visited[nnr][nnc]:
                    visited[nnr][nnc] = 1

                    if bokdo[nnr][nnc] == "O":
                        break
                    if bokdo[nnr][nnc] == "T":
                        dfs(nnr, nnc)
                        break
                    if bokdo[nnr][nnc] == "S":
                        if obstacles == 0:
                            ans = "NO"
                            return
                        bokdo[nr][nc] = "O"
                        obstacles -= 1
                        break


N = int(input())
bokdo = [list(input().split()) for _ in range(N)]
teachers = []
for i in range(N):
    for j in range(N):
        if bokdo[i][j] == 'T':
            teachers.append((i, j))

visited = [[0] * N for _ in range(N)]
ans, obstacles = "YES", 3
for teacher in teachers:
    R, C = teacher
    if not visited[R][C]:
        visited[R][C] = 1
        dfs(R, C)

print(ans)