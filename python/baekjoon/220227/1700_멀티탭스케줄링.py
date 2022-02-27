import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
gigi = list(map(int, input().split()))
locked = [0] * N
ans = 0

# 패작 2
# 소요시간 90분
# 처음 꼽을때는 일단 다 꼽음
# 다음 기기가 꼽혀있는게 아니라면, 그 뒤에 안 꼽아도 되는 기기를 뽑자
# 반복
n, w = 0, 0
while 0 in locked:
    if gigi[n] not in locked:
        locked[w] = gigi[n]
        w += 1
    n += 1

for j in range(n, K):
    if gigi[j] in locked:   # 1. 다음 기기가 이미 꼽혀있는 경우
        pass
    else:                   # 2. 다음 기기가 안 꼽혀있는 경우
        # 3. 다음 기기의 다음 기기를 확인해서 꼽혀있는 기기와 일치하면, 일치하지 않은 기기를 뽑고 2.번의 기기를 꽂자
        if j != K-1:    # 마지막 기기가 아닌 경우만 실행
            i = 1
            while j+i < K-1 and gigi[j+i] not in locked:
                i += 1
            for index, value in enumerate(locked):
                if value != gigi[j+i]:
                    locked[index] = gigi[j]
                    ans += 1
                    break
        else:               #마지막 기기가 꼽혀있지 않은거라면 뽑은 횟수 하나 추가
            if gigi[j] not in locked:
                ans += 1
print(ans)



# 패작 : 반례 2 15
#            3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
# 멀티탬 한개만 남기고 가장 많이 꼽는 용품들은 계속 꼽아 놓음
# 안 꼽힌 용품들의 횟수 count == 정답

# N, K = map(int, input().split())
# gigi = list(map(int, input().split()))
# permanently_locked = []
# ans = 0
#
# for i in range(N):
#     most_used_num, most_used_gigi = 0, 0
#     for j in range(K):
#         temp = gigi.count(gigi[j])
#         if temp > most_used_num and gigi[j] not in permanently_locked:
#             most_used_num = temp
#             most_used_gigi = gigi[j]
#     permanently_locked.append(most_used_gigi)
#
# for i in range(K):
#     if gigi[i] not in permanently_locked:
#         ans += 1
#
# print(ans)