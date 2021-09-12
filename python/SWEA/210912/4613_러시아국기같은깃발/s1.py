import sys
sys.stdin = open('input.txt')


# 소요시간 37분
# thought process: 50초
# 패작 4 와 비슷하게 하되,
# 리스트에 색을 기록해서 코드의 가독성을 높여보자

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    record = ['W'] + [0] * (N-2) + ['R']
    # 첫줄과 마지막줄은 미리 페인트
    ans = flag[0].count('B') + flag[0].count('R') + flag[-1].count('W') + flag[-1].count('B')

    for i in range(1, N-1):
        w, b, r = flag[i].count('W'), flag[i].count('B'), flag[i].count('R')
        if i+1 == N-1:                                              # 마지막에서 두번째 칸일 경우
            if record[i-1] != 'R':                                  # 파란색 & 빨간색 페인트 가능 할때
                if b >= r:                                          # 파란색 페인트 많이 되어있으면
                    ans += flag[i].count('W') + flag[i].count('R')  # 파랗게 페인트
                    record[i] = 'B'
                else:                                               # 빨갛게 페인트 많이 되어있으면
                    ans += flag[i].count('W') + flag[i].count('B')  # 빨갛게 페인트
                    record[i] = 'R'
            else:                                               # 빨간색 페인트만 가능하면
                ans += flag[i].count('W') + flag[i].count('B')  # 빨간색 페인트
                record[i] = 'R'

        elif record[i-1] == 'W':                                # 하얀 or 파랑 페인트 가능
            if w >= b:                                          # 하얀 페인트 많이 되어있으면
                ans += flag[i].count('B') + flag[i].count('R')  # 하얗게 페인트하고
                record[i] = 'W'                                 # 색 기록 남김
            else:                                               # 파랑 페인트 많이 되어있으면
                ans += flag[i].count('W') + flag[i].count('R')  # 파랗게 페인트 하고
                record[i] = 'B'                                 # 색 기록 남김

        elif record[i-1] == 'B':                                # 파랑 or 빨강 페인트 가능
            if b >= r:                                          # 파랑 페인트 많이 되어있으면
                ans += flag[i].count('W') + flag[i].count('R')  # 파랗게 페인트 하고
                record[i] = 'B'                                 # 색 기록 남김
            else:                                               # 빨강 페인트 많이 되어있으면
                ans += flag[i].count('W') + flag[i].count('B')  # 빨갛게 페인트 하고
                record[i] = 'R'                                 # 색 기록 남김

        else:                                                   # 빨갛게만 페인트 가능하면
            ans += flag[i].count('W') + flag[i].count('B')      # 빨갛게 페인트 하고
            record[i] = 'R'                                     # 색 기록 남김
    print('#{} {}'.format(tc, ans))





# # 패작 4
# # 소요시간 30분 50초
# # thought process: 50초
# # 2차원 배열로 접근해서, 하나한 수정하면서
# # 패작3 와 비슷한 맥락으로 접근하자
#
# for tc in range(int(input())):
#
#     N, M = map(int, input().split())
#     flag = [list(map(str, input())) for _ in range(N)]
#     # 첫줄과 마지막줄은 미리 페인트
#     ans = flag[0].count('B') + flag[0].count('R') + flag[-1].count('W') + flag[-1].count('B')
#
#     for i in range(1, N-1):
#         w, b, r = flag[i].count('W'), flag[i].count('B'), flag[i].count('R')
#
#         if i+1 == N:                                      # 마지막에서 2번째 줄
#             if r >= b:                                      # 빨간색을 칠할 수 있고 빨간색이 많을경우
#                 for j in range(M):                          # 빻갛게 페인트
#                     if flag[i][j] != 'R':
#                         flag[i][j] = 'R'
#                         ans += 1
#             else:
#                 for j in range(M):                          # 빻갛게 페인트
#                     if flag[i][j] != 'B':
#                         flag[i][j] = 'B'
#                         ans += 1
#         else:
#             if 'B' not in flag[i-1] and w >= b:
#                 for j in range(M):
#                     if flag[i][j] != 'W':
#                         flag[i][j] = 'W'
#                         ans += 1
#             elif 'R' not in flag[i-1] and w < b:
#                 for j in range(M):
#                     if flag[i][j] != 'B':
#                         flag[i][j] = 'B'
#                         ans += 1
#             elif r >= b:
#                 for j in range(M):
#                     if flag[i][j] != 'R':
#                         flag[i][j] = 'R'
#                         ans += 1
#     print(ans)





# # 패작 3
# # 소요시간 16분 30초
# # thought process: 4분
# # 처음부터 하얗게 페인트 하면서 마지막 두칸 남으면 강제로 파란색 빨간색 순으로 칠하기
#
# for tc in range(int(input())):
#
#     N, M = map(int, input().split())
#     flag = [input() for _ in range(N)]
#     ans = flag[0].count('R') + flag[0].count('B') + flag[-1].count('B') + flag[-1].count('W')
#
#     for i in range(1, N-1):
#         # 자리가 2개남았을때 무조건 파랑, 빨강 페인트 후 종료
#         if i+2 == N:
#             ans += flag[i].count('W') + flag[i].count('R')
#             ans += flag[i+1].count('B') + flag[i+1].count('W')
#             break
#         elif flag[i-1].count('W') >= flag[i-1].count('B') and flag[i].count('W') >= flag[i].count('B'):
#             # 하연색 페인트
#             ans += flag[i].count('B') + flag[i].count('R')
#         else:
#             # 파란색 페인트
#             if flag[i-1].count('B') >= flag[i-1].count('R') and flag[i].count('B') >= flag[i].count('R'):
#                 ans += flag[i].count('W') + flag[i].count('R')
#             # 빨간색 페인트
#             else:
#                 ans += flag[i].count('B') + flag[i].count('W')
#     print(ans)



# 패작 2
# thought process: 4분 23초
# 풀이 시간: 1시간 13분
# 맨 위와 맨 이래는 재외하고 가우데에서 가장 파란색을 적게 칠해도 되는곳을 찾고,
# 거기를 기준으로 위 는 하얗게, 아래는 빨갛게 칠하자

# for tc in range(int(input())):
#     N, M = map(int, input().split())
#     flag = tuple([input() for _ in range(N)])
#     check = [0] * N                 # 1 = 하얗, 2 = 파랑, 3 = 빨강
#     center = 0                      # 가운데 인덱스 위치 생성
#     ans = 0
#
#     # 맨 윗부분 페인트
#     w = M - flag[0].count('W')
#     ans += w
#     check[0] = 1
#
#     # 맨 아래부분 페인트
#     r = M - flag[-1].count('R')
#     ans += r
#     check[-1] = 3
#
#     # 가운데 파랑 페인트칠
#     b = 0
#     for i in range(1, N-1):
#         temp = flag[i].count('B')
#         if temp > b:
#             b = temp
#             check[i-1] = 1
#             check[i] = 2
#             center = i
#     ans += b
#
#     # 남은 윗 부분 처리
#     for i in range(1, check.index(2)):
#         # 하얗게 페인트
#         if check[i-1] == 1 and flag[i].count('W') >= flag[i].count('B'):
#             ans += flag[i].count('B') + flag[i].count('R')
#             check[i] = 1
#         # 파랗게 페인트
#         else:
#             ans + flag[i].count('W') + flag[i].count('R')
#             check[i] = 2
#         # 모든 상반 행이 칠해지면 강제 종료
#         if 0 not in check[:center]:
#             break
#     # 남은 아랫 부분 처리
#     for i in range(check.index(2)+1, M-1):
#         # 파랗게 페인트
#         if check[i-1] == 2 and flag[i].count('B') >= flag[i].count('R'):
#             ans += flag[i].count('W') + flag[i].count('R')
#             check[i] = 2
#         # 빨갛게 페인트
#         else:
#             ans += flag[i].count('W') + flag[i].count('B')
#             check[i] = 3
#         # 모든 하반 행이 칠해지면 강제 종료
#         if 0 not in check[center:check.index(3, -1)]:
#             break
#     print(ans)


#패작 1
# 미완료 풀이시간 1시간25분
# thought process: 17분10초
# 첫 줄과 마지막 줄은 무조건 백색과 적색으로 칠한다,
# 나머지 칸에서 가장 파란색을 적게 칠해도 되는곳을 파란색으로 칠하고
# 이후에 나머지 칸들을 돌아가며 가장 적게 칠해도 되는걸 찾는다

# for tc in range(1, int(input())+1):
#
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]     # 2차원 인풋값
#     ans = 0                                     # 최소 색칠값 생성
#
#     ans += M - arr[0].count('W')        # 무조건 첫줄은 백색,
#     ans += M - arr[-1].count('R')       # 마지막줄은 적색으로 칠한 횟수 ans 에 축적
#
#     min_b = 10000000000
#     idx_b = 0
#     for i in range(1, N-1):             # 첫줄과 마지막 줄 제외, 가장 파란색을 적게 칠하는곳 찾기
#         temp = M - arr[i].count('B')
#         if min_b > temp:
#             temp = min_b
#             idx_b = i                   # 파란색 색칠한 인덱스(위치) 값 저장
#     ans += min_b                        # 적게 색칠한 파란색 개수 ans 에 축적
#
#     # 남은 줄 색칠 판별
#     # 문제: 이대로가면 백파적 순서가 뒤죽박죽
#     # 고로: 파란색 기준으로 위 아래 나누어서 색칠 결정
#     # 위 반
#     w_b = [0, 0]
#     for i in range(1, idx_b):
#         w = arr.count('W')
#         b = arr.count('B')
#         if w < b:
#             w_b[1] += 1
#         else:
#             w_b[0] += 1
#     if w_b[0] > w_b[1]:
#         for i in range(1, idx_b):
#             w = arr.count('W')
#             b = arr.count('B')
#             for j in range(M):
#                 if w > b and arr[i-1][j] == 'W':
#                     temp = M - arr[i].count('W')
#                     ans += temp
#                 elif w < b and arr[i-1][j] == 'B':
#                     temp = M - arr[i].count('B')
#                     ans += temp
#                 elif arr[i-1][j] == 'W':
#                     temp = M - arr[i].count('W')
#                     ans += temp
#                 elif arr[i-1][j] == 'B':
#                     temp = M - arr[i].count('B')
#                     ans += temp
#     # 아래 반
#     r_b = [0, 0]
#     for i in range(idx_b+1, N+1):
#         r = arr.count('R')
#         b = arr.count('B')
#         if r < b:
#             r_b[1] += 1
#         else:
#             r_b[0] += 1
#     if r_b[0] > r_b[1]:
#         for i in range(idx_b+1, N+1):
#             r = arr.count('R')
#             b = arr.count('B')
#             for j in range(M):
#                 if r > b and arr[i - 1][j] == 'R':
#                     temp = M - arr[i].count('R')
#                     ans += temp
#                 elif r < b and arr[i - 1][j] == 'B':
#                     temp = M - arr[i].count('B')
#                     ans += temp
#                 elif arr[i - 1][j] == 'R':
#                     temp = M - arr[i].count('R')
#                     ans += temp
#                 elif arr[i - 1][j] == 'B':
#                     temp = M - arr[i].count('B')
#                     ans += temp









