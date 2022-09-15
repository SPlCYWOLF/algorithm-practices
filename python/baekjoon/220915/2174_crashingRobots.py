import sys
sys.stdin = open('input.txt')

# n -> e -> s -> w       # 세로 반전인것을 방향델타로 맞춰주고, 실제 field는 노터치
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def commandL(target_info):
    pass
def commandR(target_info):
    pass
def commandF(target_info):


def converter(n):
    if n.isnumeric():
        return int(n)
    return n

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = [tuple(map(converter, input().split())) for _ in range(N)]
orders = [list(map(converter, input().split())) for _ in range(M)]  # 대상 로봇, 명령의 종류, 명령의 반복 회수
field = [[0] * A for _ in range(B)]
for robot in robots:
    c, r, direction = robot
    field[r][c] = direction


for order in orders:

    target, command, repeat = order
    target_info = robots[target-1]

    for i in range(repeat):
        if command == "L":
            commandL(target_info)
        elif command == "R":
            commandR(target_info)
        else:
            commandF(target_info)