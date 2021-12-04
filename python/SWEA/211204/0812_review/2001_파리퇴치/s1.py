import sys
sys.stdin = open('input.txt')


# 처음 총 풀이시간 1시간 20분 42초
# 이번 총 풀이시간 12분

for tc in range(1, int(input())+1):

    N, c = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N-c+1):
        for j in range(N-c+1):
            temp = 0
            for k in range(c):
                for l in range(c):
                    temp += arr[i+k][j+l]
            if temp > max_kill:
                max_kill = temp
    print('#{} {}'.format(tc, max_kill))
