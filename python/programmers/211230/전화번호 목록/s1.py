import sys
sys.stdin = open('input.txt')


def solution(phone_book):
    temp = sorted(phone_book)
    for i in range(len(temp) - 1):
        if len(temp[i]) < len(temp[i + 1]):
            # if temp[i] in temp[i+1]:
            if temp[i + 1][:len(temp[i])] == temp[i]:  # 6번 코드랑 도데체 뭔 차이길래 이건 통과 되지;
                return False
    return True


for tc in range(1, int(input())+1):
    arr = list(map(str, input().split()))
    print('#{} {}'.format(tc, solution(arr)))