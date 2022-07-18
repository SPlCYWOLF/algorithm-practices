import sys
sys.stdin = open('input.txt')

#     우 좌 상 하
dr = (0, 0, 0, -1, 1)
dc = (0, 1, -1, 0, 0)
opposite = (0, 2, 1, 4, 3)                                  # 반대 방향 정보

N, K = map(int, input().split())

board = [[2] * (N+1)]                                       # 체스판의 정보 (N을 벗어나도 파란색으로 여김)
for i in range(N):
    board.append([2] + list(map(int, input().split())) + [2])
board.append([2] * (N+1))

cur = [[[] for j in range(N + 1)] for i in range(N + 1)]    # 돌의 위치 및 쌓인 돌 기록
mals = [[0]]                                                # 돌의 정보
for i in range(1, K+1):
    r, c, d = map(int, input().split())
    mals.append([r, c, d])
    cur[r][c].append(i)

print(cur)

turn, go = 1, True
while go and turn < 1000:
    for i in range(1, K+1):             # 모든 말을 돌며
        r, c, d = mals[i]               # 현재 말 정보 가져오고

        if len(cur[r][c]) and cur[r][c][0] == i:# 현재 말의 위치가 맨 아래 말이라면(움직일 수 있다면)
            nr, nc = r + dr[d], c + dc[d]           # 움직일 위치 가져오고

            if board[nr][nc] == 2:                  # 움직일 위치가 파란색이면
                nd = opposite[d]                        # 새로운 방향 가져오고
                onr, onc = r + dr[nd], c + dc[nd]       # 새로운 방향으로 움직일 위치 가져오고

                if board[onr][onc] == 2:                # 반대쪽도 파란색이면
                    mals[i] = [r, c, nd]                     # 말 정보에 새로운 방향만 저장, *위치는 바뀌지 않기 때문에 말 위치 최신화 x

                else:                                   # 아니라면
                    mals[i] = [onr, onc, nd]                 # 말 정보에 새로운 위치와 새로운 방향 저장
                    cur[onr][onc] += cur[r][c]               # 말 위치 최신화
                    cur[r][c] = []
                    if len(cur[onr][onc]) >= 4:              # 현재 말 위치에 4개 이상 말이 쌓여있다면
                        print(turn)                                 # 종료된 턴 반환
                        go = False                                  # 종료 신호
                        break

                # for j in range(1, K + 1):  # 겹쳐진 말이 있으면 위치를 맨 아래 말과 동기화
                #     if mals[j][0] == r and mals[j][1] == c:
                #         mals[j] = [onr, onc, mals[j][2]]

                continue

            elif board[nr][nc] == 1:        # 움직일 위치가 빨간색이면
                mals[i] = [nr, nc, d]               # 말 정보에 새로운 위치 저장
                cur[nr][nc] += cur[r][c][::-1]      # 말 위치 최신화 (말의 위치를 바꾸고 현 위치의 말들이 움직일 위치의 말들 위로 올라탐)
                cur[r][c] = []                      # 말 위치 최신화

            elif board[nr][nc] == 0:        # 움직일 위치가 하얀색이면
                mals[i] = [nr, nc, d]           # 말 정보 최신화
                cur[nr][nc] += cur[r][c]        # 말 위치 최신화
                cur[r][c] = []

            if len(cur[nr][nc]) >= 4:       # 현재 말 위치에 4개 이상 말이 쌓여있다면
                print(turn)                     # 종료된 턴 반환
                go = False                      # 종료 신호
                break

            for j in range(1, K+1):         # 겹쳐진 말이 있으면 위치를 맨 아래 말과 동기화
                if mals[j][0] == r and mals[j][1] == c:
                    mals[j] = [nr, nc, mals[j][2]]

    turn += 1           # 턴 종료시 +1

if go and turn == 1000:        # 1000번 이상 턴 소요시
    print(-1)               # -1 반환




# 패작2
# #     우 좌 상 하
# dr = (0, 0, -1, 1)
# dc = (1, -1, 0, 0)
#
# def on_white(nr, nc, r, c, num):
#     global cnt
#     if mals[nr][nc][0]:
#         mals[nr][nc] += mals[r][c]
#         temp[num][3] = 'on'
#         cnt += 1
#     else:
#         mals[nr][nc] = mals[r][c]
#     mals[r][c] = [0]
#     temp[num][0], temp[num][1] = nr, nc
#
# def on_red(nr, nc, r, c, num):
#     global cnt
#     if mals[nr][nc][0]:
#         mals[nr][nc] += mals[r][c]
#         mals[nr][nc] = mals[nr][nc][::-1]
#         temp[num][3] = 'on'
#         temp[mals[nr][nc][0]][3] = 'go'
#         cnt += 1
#     else:
#         mals[nr][nc] = mals[r][c]
#         mals[nr][nc] = mals[nr][nc][::-1]
#         temp[num][3] = 'on'
#         temp[mals[nr][nc][0]][3] = 'go'
#     mals[r][c] = [0]
#     temp[num][0], temp[num][1] = nr, nc
#
# def on_blue(nr, nc, r, c, num):
#     global cnt
#     if mals[nr][nc][0]:
#         mals[nr][nc] += mals[r][c]
#         temp[num][3] = 'on'
#         cnt += 1
#         mals[r][c] = [0]
#         temp[num][0], temp[num][1] = nr, nc
#         return
#
#     if temp[num][2] == 1:
#         temp[num][2] = 2
#     elif temp[num][2] == 2:
#         temp[num][2] = 1
#     elif temp[num][2] == 3:
#         temp[num][2] = 4
#     else:
#         temp[num][2] = 3
#
#
# def outside(nr, nc, r, c, num):
#     if temp[num][2] == 1:
#         temp[num][2] = 2
#     elif temp[num][2] == 2:
#         temp[num][2] = 1
#     elif temp[num][2] == 3:
#         temp[num][2] = 4
#     else:
#         temp[num][2] = 3
#
# N, K = map(int, input().split())
# board = [tuple(map(int, input().split())) for _ in range(N)]
# temp = [list(map(int, input().split()))+['go'] for _ in range(K)]
# print(temp)
# mals = [[[0]]*N for _ in range(N)]
# print(mals)
# for i in range(1, K+1):
#     r, c, direction, status = temp[i-1]
#     mals[r-1][c-1] = [i]
# print(mals)
#
# cnt = 1
# loop = 0
#
# while loop < 1000 or cnt == 4:
#     for i in range(K):
#         if temp[i][3] == 'go':
#             print(temp)
#             nr, nc = temp[i][0] + dr[temp[i][2]-1], temp[i][1] + dc[temp[i][2]-1]
#             if nr <= 0 or nr >= N or nc <= 0 or nc >= N:
#                 outside(nr, nc, temp[i][0], temp[i][1], i)
#             elif board[nr-1][nc-1] == 0:
#                 on_white(nr, nc, temp[i][0], temp[i][1], i)
#             elif board[nr-1][nc-1] == 1:
#                 on_red(nr, nc, temp[i][0], temp[i][1], i)
#             elif board[nr-1][nc-1] == 2:
#                 on_blue(nr, nc, temp[i][0], temp[i][1], i)
#     loop += 1
#
# if loop == 1000:
#     print(-1)
# else:
#     print(loop)



# 패작1
# 순서대로 말을 움직임
# 말의 위치가 겹쳐지면 말을 비활성화
# 조건에 따라서 말의 움직이는 방향 수정
# 4명에서 겹치면 끝

# 우 좌 상 하
# dr = (0, 0, -1, 1)
# dc = (1, -1, 0, 0)
#
# def move_mal(i, nr, nc):
#     if board[nr][nc] == 0:
#         mals[i][0] = nr
#         mals[i][1] = nc
#     elif board[nr][nc] == 1:
#
#
# N, K = map(int, input().split())
# board = [tuple(map(int, input().split())) for _ in range(N)]
# mals = dict()
#
# for i in range(K):
#     r, c, direction = map(int, input().split())
#     mals[i] = [r-1, c-1, direction-1, 'go', i, 0]  # row, col, 이동방향, 올라탄 여부, 맨 아래 말의 번호, 현재 위치
# print(mals)
#
# cnt = 1
# while cnt != 4:
#     for i in range(K):
#         if mals[i][3] == 'go':
#             nr, nc = mals[i][0] + dr[mals[i][2]], mals[i][1] + dc[mals[i][2]]
#             if 0 <= nr < N and 0 <= nc < N:
#                 move_mal(i, nr, nc)
#
#             for j in range(K):
#                 if i != j:
#                     if mals[i][0] == mals[j][0] and mals[i][1] == mals[j][1]:
#                         mals[i][3] = 'stop'