import sys
sys.stdin = open('input.txt')

#     우 좌 상 하
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

def on_white(nr, nc, r, c, num):
    if mals[nr][nc][0]:
        mals[nr][nc] += mals[r][c]
    else:
        mals[nr][nc] = mals[r][c]
        mals[r][c] = 0
        temp[num][3] = 'on'
def on_red(nr, nc, r, c, num):
    pass
def on_blue(nr, nc, r, c, num):
    pass

N, K = map(int, input().split())
board = [tuple(map(int, input().split())) for _ in range(N)]
temp = [list(map(int, input().split()))+['go'] for _ in range(K)]
mals = [[0]*N for _ in range(N)]
print(mals)
for i in range(1, K+1):
    r, c, direction, status = temp[i-1]
    mals[r-1][c-1] = [i]
print(mals)

cnt = 1
loop = 0

while loop < 1000:
    for i in range(K):
        if temp[i][3] == 'go':
            nr, nc = temp[i][0] + dr[2], temp[i][1] + dc[2]
            if board[nr][nc] == 0:
                on_white(nr, nc, temp[i][0], temp[i][1], i)
            if board[nr][nc] == 1:
                on_red(nr, nc, temp[i][0], temp[i][1], i)
            if board[nr][nc] == 2:
                on_blue(nr, nc, temp[i][0], temp[i][1], i)
    loop += 1

if loop == 1000:
    print(-1)
else:
    print(loop)


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