from collections import deque
import sys
sys.stdin = open('input.txt')

T, A, B = map(int, input().split())
digested = False
# bfs 활용하여 모든 경우의 수를 탐색한다

foods = [A, B]

Q = deque()
Q.append((A, T))
while Q:
    food, fullness = Q.popleft()
    fullness -= food
    if fullness == 0:
        print(T)
        break
    elif fullness:
        for i in range(2):
            Q.append((foods[i], fullness))