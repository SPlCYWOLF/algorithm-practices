import sys
sys.stdin = open('input.txt')

# 버블정렬
# 맨 앞부터 전체 값을 순회하며 숫자가 작으면 뒤에 숫자와 바꾸어가며, 순회가 끝나면 맨 뒤의 인덱스를 제외하고 같은 작업 반복

for tc in range(1, int(input())+1):

    N = int(input())
    nums = list(map(int, input().split()))
    i, done = 0, 0
    
    while N - done - 1:
        
        if nums[i] > nums[i+1]:
            nums[i+1], nums[i] = nums[i], nums[i+1]
        
        if i == N-done - 2:
            done += 1
            i = 0
        else:
            i += 1

    print('#{} {}'.format(tc, ' '.join(map(str, nums))))