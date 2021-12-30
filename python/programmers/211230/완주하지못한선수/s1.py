import sys
sys.stdin = open('input.txt')


def solution(participant, completion):
    answer = []
    # 정렬하고
    par, com = sorted(participant), sorted(completion)
    p, c, = 0, 0
    # com && par 마지막 길이 까지 도달하면 stop
    while c != len(com) and p != len(par):
        # 하나씩 돌면서 짝 지어지면 둘 다 뒤로
        if par[p] == com[c]:
            p += 1
            c += 1
        # 안 지워지면 par만 하나 뒤로
        else:
            answer.append(par[p])
            p += 1
    if not answer:
        answer.append(par[-1])

    return answer


for tc in range(1, int(input())+1):

    participant = list(map(str, input().split()))
    completion = list(map(str, input().split()))
    print('#{} {}'.format(tc, solution(participant, completion)))
