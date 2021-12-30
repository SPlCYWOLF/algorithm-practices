import sys
sys.stdin = open('input.txt')

import time
start = time.time()  # 시작 시간 저장
 
 
# 작업 코드
def finder(k, cost):
    global ans

    if k >= N:
        if ans > cost:
            ans = cost
    else:
        if cost < ans:
            for i in range(N):
                if not visited[i]:
                    visited[i] = 1
                    finder(k+1, cost+arr[k][i])
                    visited[i] = 0
            

for tc in range(1, int(input())+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 9999999999
    finder(0, 0)    # 깊이, 현재 값
    print('#{} {}'.format(tc, ans))
    
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간