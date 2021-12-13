import sys
sys.stdin = open('input.txt')

# 1번째 풀이
# for tc in range(1, int(input())+1):

#     N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
    
#     print('#{} {}'.format(tc, temp[M%N]))


# 2번째 풀이
for tc in range(1, int(input())+1):
    
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))

    front = 0
    
    for i in range(M):
        if front == N-1:
            front = 0
        else:
            front += 1
    
    print('#{} {}'.format(tc, temp[front]))