import sys
sys.stdin = open('input.txt')
from collections import deque


def finder():
    i, rounds = 0, 1
    done_cnt = 0

    while done_cnt != N:

        if needs[i] > 1:
            needs[i] -= 1
        elif needs[i] == 1:
            needs[i] -= 1
            done_cnt += 1
            ans[i] = rounds

        if i == N-1:
            i = 0
        else:
            i += 1

        if needs[i] == 0:
            continue

        rounds += 1


N = int(input())
needs = list(map(int, input().split()))
ans = [0] * N

finder()
print(*ans)