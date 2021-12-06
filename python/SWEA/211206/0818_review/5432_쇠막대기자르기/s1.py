import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    
    pipes = input()
    cnt, ans = 0, 0

    for i in range(len(pipes)):
        if pipes[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if pipes[i-1] == '(':
                ans += cnt
            else:
                ans += 1
    print('#{} {}'.format(tc, ans))