import sys
sys.stdin = open('input.txt')


dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def dfs(r, c, k, perm):
    if k >= 7:
        ans.add(perm)
        return

    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, k+1, perm*10+nums[nr][nc])


for tc in range(1, int(input())+1):

    nums = [list(map(int, input().split())) for _ in range(4)]
    ans = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, 0, 0) # 좌표, 깊이, 조합된 순열

    print('#{} {}'.format(tc, len(ans)))