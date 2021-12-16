import sys
sys.stdin = open('input.txt')


def combination(cnt):
    global ans

    temp = int(''.join(nums))       # 4. 리스트화된 nums 를 정수로 변환 (temp)

    if temp in visited[cnt]:        # 질문: 이거랑 그냥 visited 한개로 하는거랑 무슨 차이가 있길래 후자는 안될까
        return

    visited[cnt].add(temp)           # 5. cnt 번 바뀔때 마다 temp 값 집어넣기
    
    if cnt == K:
        ans = max(ans, temp)

    else:
        for i in range(N-1):
            for j in range(i+1, N):
                nums[i], nums[j] = nums[j], nums[i]
                combination(cnt+1)
                nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, int(input())+1):

    temp1, temp2 = map(str, input().split())    # 1. str로 input 불러오고
    K = int(temp2)
    N = len(temp1)
    nums = []
    nums[::] = temp1                            # 2. swap 해주기 위해 리스트화
    visited = [set() for _ in range(11)]
    ans = 0

    combination(0)                              # 3. 바꾸는 위치는 조합 기준으로, 최대 값 완전 탐색
    print('#{} {}'.format(tc, ans))