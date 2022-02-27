import sys
sys.stdin = open('input.txt')

# 소요시간 15분..
# 현 위치 기준, 정답 += (좌우측에 가장 낮은 벽 높이 - 현 위치 높이)

h, w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    highest_l = max(arr[:i])
    highest_r = max(arr[i+1:])

    current_height = arr[i]
    lower_wall = min(highest_l, highest_r)

    if lower_wall > current_height:
        ans += (lower_wall - current_height)

print(ans)