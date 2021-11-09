import sys
sys.stdin = open('input.txt')

# 출저 수민님 코드

def check(arr):
    cnt = 1
    for k in range(1, N):
        if arr[k] == arr[k-1]:
            cnt += 1
        elif arr[k] == arr[k-1] + 1 and cnt >= X:   # 높이가 1 커질 경우, 그동안 쌓아온 길이(cnt)가 경사로 길이(X)보다 크거나 같아여 가능
            cnt = 1
        elif arr[k] == arr[k-1] - 1 and cnt >= 0:   # 높이가 1 낮아질 경우, 현재 쌓아온 거리가 0보다 크거나 같다면 현재 쌓아온 거리를 음수 값으로 땡겨주어 경사로 길이만큼 같은 높이를 유지할 때 경사로를 설치할 있도록 함
            cnt = -X + 1
        else:
            return 0

    if cnt >= 0:
        return 1

    return 0


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())   # N : 지도의 한 변의 크기 X : 경사로 길이  (단, 경사로 높이는 1로 고정)
    road_row = [list(map(int, input().split())) for _ in range(N)]
    road_col = list(zip(*road_row))
    result = 0

    for i in range(N):
        result += (check(road_row[i]))
        result += (check(road_col[i]))

    print('#{} {}'.format(tc, result))