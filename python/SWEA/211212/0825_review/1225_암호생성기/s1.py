import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):

    input()
    Q = list(map(int, input().split()))
    i = 1

    while True:
        n = Q.pop(0)
        if (n - i) <= 0:
            Q.append(0)
            break
        else:
            Q.append(n-i)
            if i == 5:
                i = 1
            else:
                i += 1
    print('#{}'.format(tc), end=' ')
    print(*Q)