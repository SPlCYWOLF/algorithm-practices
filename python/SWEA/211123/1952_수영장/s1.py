import sys
sys.stdin = open('input.txt')


def calc(cost, mon):
    global min_cost
    if mon > 12:
        if min_cost < cost:
            min_cost = cost
        return
    # 1일권
    calc(cost + d * mp[mon], mon + 1)
    # 한달권
    calc(cost + m, mon + 1)
    # 3달권
    calc(cost + q, mon + 3)


for tc in range(1, int(input())+1):

    d, m, q, y = map(int, input().split())
    mp = [0] + list(map(int, input().split()))

    min_cost = y        # 1년치 비용 현재 최저가

    calc(0, 1)
    print('#{} {}'.format(tc, min_cost))