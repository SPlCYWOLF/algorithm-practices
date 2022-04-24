# 패작 bfs 활용해여 구하기

# 35분 소요 메모리 초과.
# 아마 큐의 너비가 너무 넓어져서 메모리 초과가 뜨는듯..
from collections import deque
import sys
sys.stdin = open('input.txt')

q = deque()
N = int(input())
cnt = 0
nums = [list(map(int, input().split())) for _ in range(N)]
q.append([0, 0, nums[0][0], "down"])       # 현제위치(i&j), 이동해야하는 횟수, 진행방향
q.append([0, 0, nums[0][0], "right"])
while q:
    cur = q.popleft()
    i, j = cur[0], cur[1]

    if i+1 >= N and j+1 >= N:
        cnt += 1

    if cur[2] and cur[3] == "down" and i+cur[2] < N:
        q.append([i+cur[2], j, nums[i+cur[2]][j], "down"])
        q.append([i + cur[2], j, nums[i + cur[2]][j], "right"])
    if cur[2] and cur[3] == "right" and j+cur[2] < N:
        q.append([i, j+cur[2], nums[i][j+cur[2]], "right"])
        q.append([i, j + cur[2], nums[i][j + cur[2]], "down"])

print(cnt // 2)