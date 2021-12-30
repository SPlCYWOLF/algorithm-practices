import sys
sys.stdin = open('input.txt')


def dfs(k, total):
    global ans
    if total <= ans:
        return
    if N == k:
        ans = max(total,ans)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                dfs(k+1, total*arr[k][i] / 100)
                visited[i] = 0


for tc in range(1, int(input())-98):
    
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0

    dfs(0, 100)
    print('#{} {:.6f}'.format(tc, ans))
    