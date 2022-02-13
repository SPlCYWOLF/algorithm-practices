# 작은 수의 최대 약수부터 최소 약수 순으로 탐색
# 작은것과 큰것 둘 다 약수를 찾으면 최대 공약수 해결

# 작은 수의 최소 배수 와 큰 수의 최소 배수 같은 타이밍에 찾으면 해결

# 소요시간 1시간
import sys
sys.stdin = open('input.txt')


def yaksu(n, m, i):
    global f
    if not n % i and not m % i:
        f = True


def solution():
    global f
    N, M = map(int, input().split())
    # n이 작고 m이 큰 수
    if N < M:
        n, m = N, M
    else:
        n, m = M, N

    for i in range(n, 0, -1):
        yaksu(n, m, i)
        if f:
            print(i)
            break
        # if i == N:  # 최대 공약수가 없을 시       # 왜 이게 없어지니까 정답이 되는거지?
        #     print(1)

    f = False

    i, j = 1, 1
    while not f:
        if (n * i) < (m * j):
            i += 1
        elif (n * i) > (m * j):
            j += 1
        else:
            print(n * i)
            f = True
    f = False


f = False
solution()