from collections import deque
import sys
sys.stdin = open('input.txt')

def addTime(n):
    return [int(n), 1]

N, W, L = map(int, input().split())
temp = map(addTime, input().split())
trucks = deque(temp)

# 데큐에 트럭 하나씩 넣으며 총 무게는 따로 변수를 만들어 관리.
# while문을 돌며 이동 시간을 관리하며 한칸씩 차량 이동

# 접근 가능 조건 : 무게 변수가 L 이하이고, 데큐가 꽉 차지 않은 상태에 트럭 접근 가능
on_bridge = deque()
time = 1
on_bridge.append(trucks.popleft())
cur_w, cur_n = on_bridge[0][0], 1

while on_bridge:
    cnt1 = 0
    for k in range(len(on_bridge)):
        w, t = on_bridge[k]
        if t == W:
            cur_w -= w
            cur_n -= 1
            cnt1 += 1
        else:
            on_bridge[k][1] += 1

    for l in range(cnt1):
        on_bridge.popleft()


    if trucks and cur_w + trucks[0][0] <= L and cur_n < W:
        on_bridge.append(trucks[0])
        cur_w += trucks[0][0]
        cur_n += 1
        trucks.popleft()

    time += 1

print(time)