import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    
    print('#{}'.format(tc))
    
    for i in range(N):
        for j in range(N-1, -1, -1):
            print(nums[j][i], end='')
        print(end=' ')
        
        for j in range(N-1, -1, -1):
            print(nums[N-cnt][j], end='')
        print(end=' ')
        
        for j in range(N):
            print(nums[j][N-cnt], end='')
        print(end=' ')
        
        print()
        cnt += 1