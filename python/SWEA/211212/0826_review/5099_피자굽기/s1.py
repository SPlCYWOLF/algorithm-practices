import sys
sys.stdin = open('input.txt')

# 풀이
# front 로 돌면서 위치 파악
# 다시 처음 위치로 돌아오면 모든 pizza 값 // 2
# pizza의 크기가 0혹은 아래가 되면 꺼내고 새로운 피자를 append
# 반복

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    fire = [i for i in range(N)]
    
    next = N
    while len(fire) > 1:
        i = fire.pop(0)
        pizza[i] = pizza[i] // 2
        if pizza[i] > 0:
            fire.append(i)
        elif next < M:      # 남은 피자의 수가 화덕 크기보다 더 크면 (아직 피자가 남음)
            fire.append(next)
            next += 1
    ans = fire[0] + 1
    print('#{} {}'.format(tc, ans))
    
