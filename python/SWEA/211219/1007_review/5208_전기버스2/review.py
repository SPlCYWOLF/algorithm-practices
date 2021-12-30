import sys
sys.stdin = open('input.txt')

def finder(idx, cnt, move):
    global ans
    if idx >= N:
        if ans > cnt:
            ans = cnt
    else:
        if move > 0:            # 아직 이동 가능하면 진행
            finder(idx+1, cnt, move-1)
        if ans > cnt:          # 현재 최소 교환횟수를 넘기지 않았을 시에만 배터리 교환하고 진행 (가지치기)
            finder(idx+1, cnt+1, B[idx-1]-1)


for tc in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    B = temp[1:]
    ans = 9999999999
    finder(1, 0, B[0])    # 현재 위치(1에서 출발), 교체 횟수, 이동 가능 횟수)
    print('#{} {}'.format(tc, ans))


    # if idx >= N:
    #     ans = min(ans, cnt)
    #     return
    
    # else:
    #     finder(idx+1, cnt+1, B[cnt+1])