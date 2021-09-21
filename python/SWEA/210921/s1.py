import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    temp = tuple(map(int, input().split()))
    arrival = set(temp)
    stock = 0
    ans = 'Possible'
    if 0 in arrival:
        ans = 'Impossible'
    else:
        for i in range(1, 11112):               # 초 단위
            if i % M == 0:                      # M 초마다 붕어빵 스톡 ++
                stock += K
            if i in arrival:                    # i초에 오는 사람 수 만큼 스톡에서 뺀다
                stock -= temp.count(i)
            if stock < 0:                       # 만약 남은 스톡이 0개 이하면,
                ans = 'Impossible'              # 루프 끝
                break
    print('#{} {}'.format(tc, ans))