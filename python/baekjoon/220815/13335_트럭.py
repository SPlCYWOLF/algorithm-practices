from collections import deque
import sys
sys.stdin = open('input.txt')

def addTime(n):
    return [int(n), 1]

N, W, L = map(int, input().split())
temp = map(addTime, input().split())
trucks = deque(temp)

# 데큐활용하여 큐 속도 O(1)로 단축,
# 현재 무게, 현재 다리 위 트럭 개수, 경과시간은 따로 변수를 만들어 관리.
# while문을 돌며 다리 진입, 한칸씩 차량 이동, 다리 퇴출 관리

# 접근 가능 조건 : 무게 변수가 L 이하이고, 데큐가 꽉 차지 않은 상태에 트럭 접근 가능
on_bridge = deque()
on_bridge.append(trucks.popleft())
cur_w, cur_n = on_bridge[0][0], 1
time = 1

while on_bridge:
    cnt1 = 0    # for loop 내부에서 popleft 해버리면 관리하기 번거로움, 고로 pop될 트럭 개수 cnt1에 저장
    for k in range(len(on_bridge)):     # 움직이기 직전에 현재 다리 위의 트럭 확인 작업
        w, t = on_bridge[k]     # 각 트럭의 무게, 다리 위의 위치
        if t == W:              # 다리의 끝에 위치해 있다면 (이번에 움직이면 다리에서 벗어남)
            cur_w -= w          # 현재 다리의 무게 줄이고
            cur_n -= 1          # 현재 다리의 올라온 트럭 개수 줄이고
            cnt1 += 1           # 다리에서 퇴출될 트럭 개수 갱신
        else:                       # 아직 다리 끝이 아니라면
            on_bridge[k][1] += 1    # 트럭 한칸 이동

    for l in range(cnt1):       # 트럭들 퇴출하며 현재 다리 위의 트럭 정보 갱신
        on_bridge.popleft()


    if trucks and cur_w + trucks[0][0] <= L and cur_n < W:  # 다음 트럭이 다리에 진입 가능하다면
        on_bridge.append(trucks[0])     # 다리에 트럭을 이동시키고
        cur_w += trucks[0][0]           # 현재 다리 무게 갱신
        cur_n += 1                      # 현재 다리 올라온 트럭 개수 갱신
        trucks.popleft()                # 대기중인 트럭 정보 갱신

    time += 1       # 시간 갱신

print(time)