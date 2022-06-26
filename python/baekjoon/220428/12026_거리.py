# dfs + memoization 풀이, 하지만 실패

import sys
sys.stdin = open('input.txt')

def dfs(b, cur, k, check):      # 현재 블록 정보, 현재 위치, 누적된 이동 에너지, BOJ 모두 방문 여부
    global ans, memo
    if cur == N and len(check) == 3:
        ans = min(ans, k)

    if k >= ans:
        return

    if memo[cur] < k:
        return

    for i in range(cur, N):

        if b != 3 and blocks[i] == b + 1:
            if blocks[i] not in check:      # 순서를 정확히 check 하려면 reset 과정 필요하지않을까(딕서녀리 활용 check) - 수민님
                check.append(blocks[i])
            energy = (i+1) - cur
            memo[i+1] = min(memo[i+1], k + energy*energy)
            dfs(blocks[i], i+1, k + energy*energy, check)

        elif b == 3 and blocks[i] == 1:
            if blocks[i] not in check:
                check.append(blocks[i])
            energy = (i+1) - cur
            memo[i+1] = min(memo[i+1], k + energy*energy)
            dfs(blocks[i], i+1, k + energy*energy, check)


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
memo = [10000] * (N+1)
ans = 10000

dfs(blocks[0], 1, 0, [])    # 현재 블록 정보, 현재 위치, 누적된 이동 에너지, BOJ 모두 방문 여부

if ans == 10000:
    print(-1)
else:
    print(ans)