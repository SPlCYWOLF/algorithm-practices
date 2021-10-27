'''

주사위를 던진 횟수 N과 출력형식 M을 입력 받아서 M의 값에 따라 각각 아래와 같이 출력하는 프로그램을 작성하시오.


M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우       => 중복 순열
M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우       => 순열
M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우          => 조합

'''
import sys
sys.stdin = open('input.txt')


def perm(r):            # 중복순열
    if r == N:
        print(*ans)
        pass
    else:
        for i in range(1, 7):
            ans[r] = i
            perm(r+1)

def comb(r):            # 중복조합
    if r == N:
        a = tuple(sorted(ans2))
        if a not in tmp:
            tmp.add(a)
            print(*ans2)
    else:
        for i in range(1, 7):
            ans2[r] = i
            comb(r+1)

def molla(r):       # 순열
    if r == N:
        print(*ans3)
    else:
        for i in range(1, 7):
            ans3[r] = i
            if ans3[r] != ans3[r-1] and ans3[r] != ans3[r-2]:
                molla(r+1)
            ans3[r] = 0

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans, ans2, ans3 = [0, 0, 0], [0, 0, 0], [0, 0, 0]
    tmp = set()
    if M == 1:
        perm(0)
        print('---------------------------')
    elif M == 2:
        comb(0)
        print('---------------------------')
    else:
        molla(0)
        print('---------------------------')



def perm_visited(k):
    if k == 3:
        print(visited)
        return
    else:
        for i in range(1, 4):
            visited[k] = i
            if visited[k] != visited[k-1] and visited[k] != visited[k-2]:
                perm_visited(k+1)
            visited[k] = 0


nums = [1, 2, 3]
visited = [0, 0, 0]
perm_visited(0)
