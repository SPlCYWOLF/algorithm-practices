import sys
sys.stdin = open('input.txt')


'''
thought process:

for loop 로 맨 위 row 하나씩 순회.
각 요소당 아래로 내려가면서 다음 요소값이 같은지 작은지 큰지 확인
    같으면 tmp 값 누적하며 X값 도달시 possible_up 값 true 로 변환 (초기 possible_up 값 false)
    새 위치 높이가 작으면 possible_down 값 확인해서 가능할 떄만 이동
    새 위치 높이가 크면 possible_up 값 확인해서 가능할 떄만 이동
배열 길이만큼 이동하면 ans에 개수 한개 추가

column 에서도 같은것 반복

수정사항:
# while 루프 안에 while 루프로 재구성 해보자
'''

# def checker(r, c, height, k):
#     global ans
#     if k >= N-1:
#         return
#
#     else:
#         # while 루프 안에 while 루프로 재구성 해보자
#         possible_up = False     # 처음에는 최소 한칸 전진해야
#         possible_down = True
#         tmp = 0
#         new_height = road[r+1][c]
#         while new_height == height:
#             if tmp+k == N-1:
#                 ans += 1
#                 return
#             else:
#                 tmp += 1
#                 new_height = road[r+tmp][c]
#                 if tmp >= X:
#                     possible_up = True
#                 if (N-1) - (tmp+k) < X:
#                     possible_down = False
#
#         if new_height+1 == height and possible_down:              # 새로운 높이가 더 낮을때
#             checker(r+tmp, c, new_height, k+tmp)
#
#         elif new_height-1 == height and possible_up:    # 새로운 높이가 더 높을때
#             checker(r+tmp, c, new_height, k+tmp)


def possible_down(r, c, height):
    if (r + 1) <= (N - 1):
        tmp = 1
        new_height = road[r+tmp][c]
        while (r + tmp) <= N-1 and new_height == height:
            tmp += 1
            if tmp == X:
                return True
            height = new_height
            new_height = road[r + tmp][c]

    return False

def checker(r, c, height):
    global ans
    if (r + 1) < N:
        possible_up = False
        tmp = 1
        new_height = road[r+tmp][c]

        while (r + tmp) < N-1 and new_height == height:       # 범위 벗어나지 않고 높이가 같을때
            tmp += 1
            height = new_height             # 현재 높이 갱신
            new_height = road[r+tmp][c]     # 다음 높이 갱신
            if tmp == X:                    # 경사로 세울 수 있으면
                possible_up = True          # 올라갈 수 있다!

        if r + tmp == N-1 and new_height == height:                            # 끝까지 갔으면 정답 추가
            ans += 1
            return
        elif height+1 == new_height:                # 새로운 높이가 더 높을때
            if possible_up:
                checker(r+tmp, c, new_height)
        elif height-1 == new_height:                # 새로운 높이가 더 낮을때
            if possible_down(r+tmp, c, new_height):
                checker(r+tmp, c, new_height)


for tc in range(1, int(input())+1):

    N, X = map(int, input().split())
    road = tuple(tuple(map(int, input().split())) for _ in range(N))
    if tc == 2:
        ans = 0
        for i in range(1):
            for j in range(N):
                checker(i, j, road[i][j])    # row column 좌표, 시작지점 원소값, 총 이동 거리

        road = tuple(zip(*road))
        for i in range(1):
            for j in range(N):
                checker(i, j, road[i][j])    # row column 좌표, 시작지점 원소값, 총 이동 거리
        print('#{} {}'.format(tc, ans))