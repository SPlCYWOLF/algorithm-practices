import sys
sys.stdin = open('input.txt')

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def finder(r, c):
    global obstacles, ans, cnt
    if obstacles == 0 and cnt == L:          # 설치가능 장애물이 없을 시 종료
        return

    for l in range(4):          # 선생님 기준 4방향 탐색
        nr, nc = r + dr[l], c + dc[l]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:     # 방문 가능한 위치이면

            if bokdo[nr][nc] == "S":    # 바로 옆 자리가 학생이면 무조건 발각,
                obstacles = 0           # recursion 종료 위해 obstacles 값 0으로 변환
                ans = "NO"              # 고로, 정답 : NO
                return
            if bokdo[nr][nc] == "O":    # 바로 옆 자리가 장애물이면 무조건 학생 안들키니 다른 방향으로 전환
                continue
            if bokdo[nr][nc] == "T":    # 바로 옆 자리가 선생님이면 옆 선생님 기준으로 학생 탐색 시작
                visited[nr][nc] = 1  # 방문 체크
                finder(nr, nc)
                continue                # 옆 선생님 위치에서 학생 발견되면 알아서 처리 했을테니, 탐색 방향 전환

            for k in range(1, N):       # 선택된 방향에서 계속 나아가며 학생 탐색
                nnr, nnc = nr + (dr[l] * k), nc + (dc[l] * k)

                if 0 <= nnr < N and 0 <= nnc < N and not visited[nnr][nnc]:     # 방문 가능한 위치면

                    if bokdo[nnr][nnc] == "O":  # 장애물을 만나면, 바로 방향 전환
                        break
                    if bokdo[nnr][nnc] == "T":  # 다른 선생님 만나면, 해당 선생님 기준으로 탐새 시작
                        visited[nr][nc] = 1  # 방문 체크
                        finder(nnr, nnc)
                        break                   # 학생 발견되면 알아서 처리 했을테니, 탐색 방향 전환
                    if bokdo[nnr][nnc] == "S":  # 학생 만났고
                        if obstacles == 0:      # 설치 가능한 장애물이 없다면
                            ans = "NO"          # 학생 발각, 고로 정답 : NO
                            return
                        bokdo[nr][nc] = "O"     # 장애물이 남아있다면, 장애물 설치 하고
                        obstacles -= 1          # 장애물 개수 최신화 한 뒤
                        break                   # 방향 전환
    cnt += 1

N = int(input())
bokdo = [list(input().split()) for _ in range(N)]
students = 0
teachers = []                           # 선생님 위치 저장
for i in range(N):
    for j in range(N):
        if bokdo[i][j] == "T":
            teachers.append((i, j))
        if bokdo[i][j] == "S":
            students += 1
L = len(teachers)

visited = [[0] * N for _ in range(N)]
ans, obstacles, cnt = "YES", 3, 0

if L == 0:
    pass
elif students == 0:
    pass
else:
    for teacher in teachers:                # 선생님 한명씩 돌면서
        R, C = teacher
        if not visited[R][C]:               # 확인하지 않았다면
            visited[R][C] = 1
            finder(R, C)                       # 학생 탐색 시작

print(ans)





# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# def finder(r, c):
#     global obstacles, ans, cnt
#     if obstacles == 0 and cnt == L:          # 설치가능 장애물이 없을 시 종료
#         return
#
#     for l in range(4):          # 선생님 기준 4방향 탐색
#         nr, nc = r + dr[l], c + dc[l]
#
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:     # 방문 가능한 위치이면
#             visited[nr][nc] = 1         # 방문 체크
#
#             if bokdo[nr][nc] == "S":    # 바로 옆 자리가 학생이면 무조건 발각,
#                 obstacles = 0           # recursion 종료 위해 obstacles 값 0으로 변환
#                 ans = "NO"              # 고로, 정답 : NO
#                 return
#             if bokdo[nr][nc] == "O":    # 바로 옆 자리가 장애물이면 무조건 학생 안들키니 다른 방향으로 전환
#                 continue
#             if bokdo[nr][nc] == "T":    # 바로 옆 자리가 선생님이면 옆 선생님 기준으로 학생 탐색 시작
#                 finder(nr, nc)
#                 continue                # 옆 선생님 위치에서 학생 발견되면 알아서 처리 했을테니, 탐색 방향 전환
#
#             for k in range(1, N):       # 선택된 방향에서 계속 나아가며 학생 탐색
#                 nnr, nnc = nr + (dr[l] * k), nc + (dc[l] * k)
#
#                 if 0 <= nnr < N and 0 <= nnc < N and not visited[nnr][nnc]:     # 방문 가능한 위치면
#                     visited[nnr][nnc] = 1       # 방문 체크
#
#                     if bokdo[nnr][nnc] == "O":  # 장애물을 만나면, 바로 방향 전환
#                         break
#                     if bokdo[nnr][nnc] == "T":  # 다른 선생님 만나면, 해당 선생님 기준으로 탐새 시작
#                         finder(nnr, nnc)
#                         break                   # 학생 발견되면 알아서 처리 했을테니, 탐색 방향 전환
#                     if bokdo[nnr][nnc] == "S":  # 학생 만났고
#                         if obstacles == 0:      # 설치 가능한 장애물이 없다면
#                             ans = "NO"          # 학생 발각, 고로 정답 : NO
#                             return
#                         bokdo[nr][nc] = "O"     # 장애물이 남아있다면, 장애물 설치 하고
#                         obstacles -= 1          # 장애물 개수 최신화 한 뒤
#                         break                   # 방향 전환
#     cnt += 1
#
# N = int(input())
# bokdo = [list(input().split()) for _ in range(N)]
# students = 0
# teachers = []                           # 선생님 위치 저장
# for i in range(N):
#     for j in range(N):
#         if bokdo[i][j] == "T":
#             teachers.append((i, j))
#         if bokdo[i][j] == "S":
#             students += 1
# L = len(teachers)
#
# visited = [[0] * N for _ in range(N)]
# ans, obstacles, cnt = "YES", 3, 0
#
# if L == 0:
#     pass
# elif students == 0:
#     pass
# else:
#     for teacher in teachers:                # 선생님 한명씩 돌면서
#         R, C = teacher
#         if not visited[R][C]:               # 확인하지 않았다면
#             visited[R][C] = 1
#             finder(R, C)                       # 학생 탐색 시작
#
# print(ans)






# 선생님의 숫자가 적음, 고로 선생님 기준으로 학생이 보이면 장애물 설치
# bfs 활용하여 각 선생님 기준으로 상우하좌 한칸씩 가려보며 3개의 장애물 설치가 완료되 때 마다
# 선생님 기준으로 loop 돌며 가려진 여부 확인
# 가려졌으면 YES, 아니면 NO 반환

# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# def dfs(r, c):
#     global obstacles, ans
#     if obstacles == 0:
#         return
#
#     for l in range(4):
#         nr, nc = r + dr[l], c + dc[l]
#
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#             visited[nr][nc] = 1
#
#             if bokdo[nr][nc] == "S":
#                 obstacles = 0
#                 ans = "NO"
#                 return
#             if bokdo[nr][nc] == "O":
#                 continue
#             if bokdo[nr][nc] == "T":
#                 dfs(nr, nc)
#                 continue
#
#             for k in range(1, N):
#                 nnr, nnc = nr + (dr[l] * k), nc + (dc[l] * k)
#
#                 if 0 <= nnr < N and 0 <= nnc < N and not visited[nnr][nnc]:
#                     visited[nnr][nnc] = 1
#
#                     if bokdo[nnr][nnc] == "O":
#                         break
#                     if bokdo[nnr][nnc] == "T":
#                         dfs(nnr, nnc)
#                         break
#                     if bokdo[nnr][nnc] == "S":
#                         if obstacles == 0:
#                             ans = "NO"
#                             return
#                         bokdo[nr][nc] = "O"
#                         obstacles -= 1
#                         break
#
#
# N = int(input())
# bokdo = [list(input().split()) for _ in range(N)]
# teachers = []
# for i in range(N):
#     for j in range(N):
#         if bokdo[i][j] == 'T':
#             teachers.append((i, j))
#
# visited = [[0] * N for _ in range(N)]
# ans, obstacles = "YES", 3
# for teacher in teachers:
#     R, C = teacher
#     if not visited[R][C]:
#         visited[R][C] = 1
#         dfs(R, C)
#
# print(ans)