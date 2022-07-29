import sys
sys.stdin = open('input.txt')


N, R = map(int, input().split())
returnee = list(map(int, input().split()))

if N == R:
    print('*')

else:
    temp = [x+1 for x in range(N)]
    for r in returnee:
        if r in temp:
            temp.remove(r)
    print(*temp, end=' ')