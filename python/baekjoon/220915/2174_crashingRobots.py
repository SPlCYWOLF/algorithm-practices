import sys
sys.stdin = open('input.txt')

# 로봇의 위치 & 방향 & 번호 기록 필요

# n -> e -> s -> w       # 세로 반전인것을 방향델타로 맞춰주고, 실제 field는 노터치
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def commandL(target_info, target):
    pass
def commandR(target_info, target):
    pass
def commandF(target_info, target):
    global field
    c, r, d = target_info
    



def converter(n):
    if n.isnumeric():
        return int(n)
    return n

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = [tuple(map(converter, input().split())) for _ in range(N)] # 로봇의 위치와 해당 방향 기록
orders = [list(map(converter, input().split())) for _ in range(M)]  # 대상 로봇, 명령의 종류, 명령의 반복 회수
field = [[0] * A for _ in range(B)]     # 로봇의 번호와 해당 위치 기록
for robot in robots:
    c, r, direction = robot
    field[r][c] = direction


for order in orders:

    target, command, repeat = order
    target_info = robots[target-1]

    for i in range(repeat):
        if command == "L":
            commandL(target_info, target - 1)
        elif command == "R":
            commandR(target_info, target - 1)
        else:
            commandF(target_info, target - 1)