import sys
sys.stdin = open('input.txt')

# 행 열 동시에 거꾸로 뒤집었을때 동일한 문자 찾으면 해당 문자 반환

for tc in range(1, int(input())+1):
    
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    r_arr = [''.join(x) for x in list(zip(*arr))]
    t, l = 0, 0
    i = 0
    ans = ''

    while l < N:
        while t+M <= N:
            if arr[l][t:M+t] == arr[l][t:M+t][::-1]:
                ans = arr[l][t:M+t]
                break
            if r_arr[l][t:M+t] == r_arr[l][t:M+t][::-1]:
                ans = r_arr[l][t:M+t]
                break
            t += 1
        t = 0
        l += 1

    print('#{} {}'.format(tc, ans))
