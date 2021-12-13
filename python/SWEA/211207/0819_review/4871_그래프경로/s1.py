import sys
sys.stdin = open('input.txt')


def dfs(v, e):
    global ans
    
    if v == e:
        ans = 1

    if not visited[v] and ans == 0:
        visited[v] = 1
        for w in range(1, V+1):
            if G[v][w] == 1 and not visited[w]:
                dfs(w, e)
        
        
for tc in range(1, int(input())+1):

    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    ans = 0
    for i in range(E):
        G[temp[i][0]][temp[i][1]] = 1
        
    visited = [0] * (V+1)
    dfs(start, end)
    print('#{} {}'.format(tc, ans))
    