import sys
sys.stdin = open('input.txt')

# 그냥 1초 2초 3초 5초 때 리스트를 만들어 놓고 N == 1, N % 2, N % 4 == 3, N % 4 == 1 인 경우
# 적절한 리스트를 반환
#
# 반례 :
# 3 3 5
# OO.
# OOO
# OOO

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

R, C, N = map(int, input().split())

one = list(input() for _ in range(R))
two = list('O' * C for _ in range(R))

three = list(['O'] * C for _ in range(R))
for i in range(R):
    for j in range(C):
        if one[i][j] == 'O':
            three[i][j] = '.'

            for k in range(4):
                if 0 <= i + dr[k] < R and 0 <= j + dc[k] < C:
                    three[i + dr[k]][j + dc[k]] = '.'

five = list(['O'] * C for _ in range(R))
for i in range(R):
    for j in range(C):
        if three[i][j] == 'O':
            five[i][j] = '.'

            for k in range(4):
                if 0 <= i + dr[k] < R and 0 <= j + dc[k] < C:
                    five[i + dr[k]][j + dc[k]] = '.'

if N == 1:
    for i in range(R):
        print(one[i])

elif N % 2 == 0:
    for i in range(R):
        print(two[i])

elif N % 4 == 1:
    for i in range(R):
        print(''.join(five[i]))

elif N % 4 == 3:
    for i in range(R):
        print(''.join(three[i]))


# ....  1
# OO..
# OO..
# OO..
#
# OOOO  2
# OOOO
# OOOO
# OOOO
#
# ..OO  3
# ...O
# ...O
# ...O
#
# OOOO  4
# OOOO
# OOOO
# OOOO
#
# O...  5
# OO..
# OO..
# OO..








# 패작1
# N이 짝수면 무조건 풀 000000리스트 반환
# 홀수면 진행
# 일단 첫 주어진 격자판 상태 가져옴

# cnt + 2, 폭탄 사정거리 밖에 있고 폭탄이 없는 위치들 전부 리스트에 저장
# N에 도달할때 까지 반복

# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# R, C, N = map(int, input().split())
#
# if not N % 2:
#     for _ in range(R):
#         print('O' * C)
#
# else:
#     cnt = 1
#     board = list(input() for _ in range(R))
#     while cnt != N:
#         cnt += 2
#         for i in range(R):
#             for j in range(C):
#                 good = 0
#                 cur = board[i][j]
#                 if cur == 'O':
#                     continue
#
#                 for k in range(4):
#                     if 0 > i+dr[k] and i+dr[k] >= R and 0 > j+dc[k] and j+dc[k] >= C:
#                         good += 1
#                         continue
#
#                     n_cur = board[i+dr[k]][j+dc[k]]
#                     if n_cur != 'O':
#                         good += 1
#
#                 if good == 4:

