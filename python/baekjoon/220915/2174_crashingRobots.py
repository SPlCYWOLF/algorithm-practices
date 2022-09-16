import sys
sys.stdin = open('input.txt')

# 로봇의 위치 & 방향 & 번호 기록 필요

# n -> e -> s -> w       # 세로 반전인것을 방향델타로 맞춰주고, 실제 field는 노터치
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
dir = {"N": 0, "E": 1, "S": 2, "W": 3}

def commandL(target_info, target):
    c, r, d = target_info
    cur_dir = robots[target - 1][2]

    if cur_dir == "N":
        robots[target - 1][2] = "W"
    elif cur_dir == "E":
        robots[target - 1][2] = "N"
    elif cur_dir == "S":
        robots[target - 1][2] = "E"
    else:
        robots[target - 1][2] = "S"

def commandR(target_info, target):
    c, r, d = target_info
    cur_dir = robots[target-1][2]

    if cur_dir == "N":
        robots[target - 1][2] = "E"
    elif cur_dir == "E":
        robots[target - 1][2] = "S"
    elif cur_dir == "S":
        robots[target - 1][2] = "W"
    else:
        robots[target - 1][2] = "N"

def commandF(target_info, target):
    global field
    c, r, d = target_info

    nc, nr = c + dy[dir[d]], r + dx[dir[d]]

    if 0 < nc <= A and 0 < nr <= B:     # 벽에 no crash
        if field[nr][nc] == 0:          # 로봇에 no crash 했다면 ↓
            field[r][c] = 0             # 현재위치 에서 벗어나서
            field[nr][nc] = target      # 새로운 위치로 이동 기록
            robots[target-1] = [nc, nr, d]  # 로봇의 현재 위치 갱신
            return True

        print(f"Robot {target} crashes into robot {field[nr][nc]}")     # 로봇에 crash 했다면
        return False        # 종료 신호

    print(f"Robot {target} crashes into the wall")          # 벽에 crash 했다면
    return False            # 종료 신호


def converter(n):
    if n.isnumeric():
        return int(n)
    return n

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = [list(map(converter, input().split())) for _ in range(N)] # 로봇의 위치와 해당 방향 기록
orders = [list(map(converter, input().split())) for _ in range(M)]  # 대상 로봇, 명령의 종류, 명령의 반복 회수
field = [[0] * (A+1) for _ in range(B+1)]     # 로봇의 번호와 해당 위치 기록
for i, robot in enumerate(robots):
    c, r, direction = robot
    field[r][c] = i + 1

end = False
for order in orders:

    target, command, repeat = order

    for i in range(repeat):
        target_info = robots[target - 1]

        if command == "L":
            commandL(target_info, target)
        elif command == "R":
            commandR(target_info, target)
        else:
            if not commandF(target_info, target):
                end = True
                break

    if end:
        break

if not end:
    print("OK")