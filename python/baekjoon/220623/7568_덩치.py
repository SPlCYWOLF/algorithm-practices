import sys
sys.stdin = open('input.txt')


N = int(input())
profile = [list(map(int, input().split())) for _ in range(N)]
ans = []

for i in range(N):      # 모든 profile을 돌면서
    w, h = profile[i]   # 각 사람의 몸무게와 키 변수 저장
    rank = 1            # 해당 사람의 순위 선언
    for j in range(N):  # profile 모든 사람들의 몸무게와 키를 자신과 비교,
        if w < profile[j][0] and h < profile[j][1]: # 본인보다 덩치가 크면
            rank += 1                               # 본인의 순위 한단계 아래로
    ans.append(rank)    # 본인의 최종 순위 저장

print(*ans)             # 저장된 순위 리스트 출력