import sys
sys.stdin = open('input.txt')


# 한칸식 전진하면서 나보다 크면 temp 갱신
# 나보다 작으면 cnt+1 & 범위내의 다음으로 작은 수 지정
# cnt = 2 되면 범위내의 다음으로 작은 수를 뺀 수를 ans 에 저장
# 위의 과정을 반복
for tc in range(1, 3):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        second = max(nums[i-2], nums[i-1], nums[i+1], nums[i+2])
        me = nums[i]
        if me > second:
            ans += me - second
    print(ans)