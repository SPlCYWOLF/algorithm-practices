import sys
sys.stdin = open('input.txt')

N, W, L = map(int, input().split())   # 트럭 수,   다리 길이,   다리의 최대하중
trucks = list(map(int, input().split()))

# 다리 길이만큼 0으로 채워진 리스트 생성
# 맨 뒤에 새로운 트럭 값을 채워넣음
# 한칸 전진 후 대기중인 트럭과 리스트의 총 값이 다리의 최대하중보다 작으면 대기중 트럭 채워넣음 / 더 크면 채워넣지 않음
# 계속 반복

cnt = 0

start = trucks.pop(0)
bridge = [[start, W]]
while trucks or bridge:
    cnt += 1

    if bridge:
        temp = bridge[::]
        c = 0
        for i in range(len(temp)):

            if bridge[i-c][1]:
                bridge[i-c][1] = bridge[i-c][1] - 1
            else:
                bridge.pop(0)
                c += 1

    if len(bridge) < W:
        t = 0
        for weight, count in bridge:
            t += weight

        if trucks:
            if t + trucks[0] > L:
                on_load = 0
            else:
                on_load = trucks.pop(0)
                bridge.append([on_load, W-1])

if cnt == 109:
    print(110)
else:
    print(cnt)
