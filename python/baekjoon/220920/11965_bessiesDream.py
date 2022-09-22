from collections import deque
import sys
sys.stdin = open('input.txt')

# 3번째 도전 : 다익스트라 활용 필요
#             참고 ㄱㄱ : https://rebas.kr/704

# 패작2 : 중복방문을 허용한 bfs로는, input의 크기가 커지면 중복이 너무 많아져서 안끝남.
#         샘플 수가 적으면 정답은 나오긴함

# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

N, M = map(int, input().split())
field = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
ans = -1

visited = [[0] * (M+2)] + [[0] + [0] * M + [0] for _ in range(N)] + [[0] * (M+2)]

Q = deque()
Q.append((1, 1, False, False, 0, 0)) # 현재위치, 현재방향, 냄새여부, 슬라이드여부, 슬라이드방향, 이동횟수
visited[1][1] = 1
found = False   # 정답 찾을 시 종료 플래그 변수
while Q:
    r, c, smells, slides, slide_d, cnt = Q.popleft()

    if slides:              # 미끄러지는 경우 처리
        nr, nc = r + dr[slide_d], c + dc[slide_d]
        if field[nr][nc]:
            if field[nr][nc] == 2:
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    break
                Q.append((nr, nc, True, False, -1, cnt + 1))

            elif field[nr][nc] == 3:
                Q.append((r, c, False, False, -1, cnt))

            elif field[nr][nc] == 4:
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    break
                Q.append((nr, nc, False, True, slide_d, cnt + 1))

            else:
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    break
                Q.append((nr, nc, False, False, -1, cnt + 1))

        else:
            Q.append((r, c, False, False, -1, cnt))

        continue


    for k in range(4):      # 안 미끄러지는 경우 처리
        nr, nc = r + dr[k], c + dc[k]

        if field[nr][nc]:
            if field[nr][nc] == 2:  # 오렌지 냄새 추가
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    found = True
                    break
                Q.append((nr, nc, True, False, -1, cnt + 1))

            elif field[nr][nc] == 3:    # 오렌지 냄새 없으면 통과 허용
                if smells:
                    visited[nr][nc] = 1
                    if nr == N and nc == M:
                        ans = cnt + 1
                        found = True
                        break
                    Q.append((nr, nc, smells, False, -1, cnt+1))

            elif field[nr][nc] == 4:    # 진행 방향으로만 진행되도록 설정
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    found = True
                    break
                Q.append((nr, nc, False, True, k, cnt + 1))

            else:
                visited[nr][nc] = 1
                if nr == N and nc == M:
                    ans = cnt + 1
                    found = True
                    break
                Q.append((nr, nc, smells, False, -1, cnt+1))

    if found:
        break

print(ans)





# 패작 1
# N, M = map(int, input().split())
# field = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
# ans = -1
#
# visited = [[0] * (M+2)] + [[0] + [0] * M + [0] for _ in range(N)] + [[0] * (M+2)]
#
# Q = deque()
# Q.append((1, 1, False, 0)) # 현재위치, 현재방향, 냄새여부, 이동횟수
# visited[1][1] = 1
# found = False   # 정답 찾을 시 종료 플래그 변수
# while Q:
#
#     r, c, smells, cnt = Q.popleft()
#
#     for k in range(4):
#         nr, nc = r + dr[k], c + dc[k]
#
#         if field[nr][nc] and not visited[nr][nc]:
#
#             if field[nr][nc] == 2:
#                 visited[nr][nc] = 1
#                 if nr == N and nc == M:
#                     ans = cnt + 1
#                     found = True
#                     break
#
#                 Q.append((nr, nc, True, cnt+1))
#
#             elif field[nr][nc] == 3:
#                 if smells:
#                     visited[nr][nc] = 1
#                     if nr == N and nc == M:
#                         ans = cnt + 1
#                         found = True
#                         break
#
#                     Q.append((nr, nc, smells, cnt+1))
#
#             elif field[nr][nc] == 4:
#                 if nr == N and nc == M:
#                     ans = cnt + 1
#                     found = True
#                     break
#
#                 moved = 1
#                 while field[nr][nc] == 4:
#                     visited[nr][nc] = 1
#                     nr, nc = nr + dr[k], nc + dc[k]
#                     moved += 1
#
#                 if field[nr][nc] == 2:
#                     if nr == N and nc == M:
#                         ans = cnt + moved
#                         found = True
#                         break
#
#                     Q.append((nr, nc, True, cnt+moved))
#
#                 elif field[nr][nc] == 3:
#                     nr, nc = nr - dr[k], nc - dc[k]
#                     Q.append((nr, nc, False, cnt + moved - 1))
#
#                 elif field[nr][nc] == 1:
#                     if nr == N and nc == M:
#                         ans = cnt + moved
#                         found = True
#                         break
#
#                     Q.append((nr, nc, False, cnt+moved))
#
#             else:
#                 visited[nr][nc] = 1
#                 if nr == N and nc == M:
#                     ans = cnt + 1
#                     found = True
#                     break
#
#                 Q.append((nr, nc, smells, cnt+1))
#
#     if found:
#         break
#
# print(ans)