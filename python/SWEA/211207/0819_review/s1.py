import sys
sys.stdin = open('input.txt')


def dfs(s, e):
    pass
        
            


for tc in range(1, int(input())+1):

    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    
    for i in range(E):
        G[temp[i][0]][temp[i][1]] = 1
        
    visited = [0 for _ in range(V+1)]
    print(visited)
    # print('#{} {}'.format(tc, dfs(start, end)))
    