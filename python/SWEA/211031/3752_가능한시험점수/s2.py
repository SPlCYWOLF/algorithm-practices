import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [1] + [0] * sum(score)
    result = [0]
    for num in score:
        for i in range(len(result)):
            temp = result[i] + num
            if not visited[temp]:
                visited[temp] = 1
                result.append(temp)
    print('#{} {}'.format(t, len(result)))