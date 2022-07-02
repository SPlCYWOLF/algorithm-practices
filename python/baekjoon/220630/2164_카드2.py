import sys
sys.stdin = open('input.txt')
from collections import deque


N = int(input())
Q = deque()

for i in range(1, N+1):
    Q.append(i)

j = 1
while len(Q) != 1:
    if j % 2:
        Q.popleft()
    else:
        temp = Q.popleft()
        Q.append(temp)
    j += 1

print(Q[0])
