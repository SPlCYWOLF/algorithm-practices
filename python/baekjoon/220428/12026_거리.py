# dfs + memoization + 가지치기로 풀이

import sys
sys.stdin = open('input.txt')

def dfs(b, cur, k):
    global ans
    if cur == N:
        ans = min(ans, k)

    for i in range(cur, N):
        if b != 3 and blocks[i] == b + 1:
            energy = (i+1) - cur
            dfs(blocks[i], i+1, k + energy)
        elif b == 3 and blocks[i] == 1:
            energy = (i+1) - cur
            dfs(blocks[i], i+1, k + energy)


def converter(n):
    if n == 'B':
        return 1
    elif n == 'O':
        return 2
    else:
        return 3

N = int(input())
blocks = input()
blocks = list(map(converter, blocks))
temp = [0] * (N+1)
ans = 1000

dfs(blocks[0], 1, 0)    # 현재 블록 정보, 현재 위치, 누적된 이동 에너지
print(ans)