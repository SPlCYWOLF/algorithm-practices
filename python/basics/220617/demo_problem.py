import sys
sys.stdin = open('input.txt')

for i in range(4):
    ans = 1
    temp = sorted(list(map(int, input().split())))
    print(temp)
    max_n, min_n = max(temp), min(temp)

    for j in range(len(temp)):
        if max_n < 1:
            break
        if min_n != 1 and max_n > 1 and 1 not in temp:  # 가장 작은 값인 1이 없을때
            break
        if 0 < j < len(temp)-1:                           # 중간에 가장 작은 수 찾기
            if temp[j + 1] != temp[j] + 1 and temp[j + 1] != temp[j]:
                ans = temp[j] + 1
                break
        else:                                           # 첫번째와 마지막 숫자 처리
            ans = temp[j] + 1
    print(ans)