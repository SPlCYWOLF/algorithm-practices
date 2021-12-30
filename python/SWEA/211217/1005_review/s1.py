import sys
sys.stdin = open('input.txt')


def run_finder2(arr2):
    global ans, cnt2
    temp2 = sorted(arr2)
    if cnt2 == 2:
        ans = 2
    else:
        for i in range(len(arr2)-1):
            if temp2[i] == temp2[i+1]-1:
                temp2.pop(i)
                cnt2 += 1
                run_finder2(temp2)


def tri_finder2(arr2):
    global ans
    for i in range(1, 10):
        if arr2.count(i) >= 3:
            ans = 2


def run_finder1(arr1):
    global ans, cnt1
    temp1 = sorted(arr1)
    if cnt1 == 2:
        ans = 1
    else:
        for i in range(len(arr1)-1):
            if temp1[i] == temp1[i+1]-1:
                temp1.pop(i)
                cnt1 += 1
                run_finder1(temp1)


def tri_finder1(arr1):
    global ans
    for i in range(1, 10):
        if arr1.count(i) >= 3:
            ans = 1


for tc in range(1, int(input())+1):

    temp = list(map(int, input().split()))
    p1, p2 = [], []
    ans = 0
    for i in range(6):
        p1.append(temp[i*2])
        p2.append(temp[i*2+1])
        if ans == 0:
            cnt1, cnt2 = 0, 0
            tri_finder1(p1)
            run_finder1(p1)
            tri_finder2(p2)
            run_finder2(p2)
        else:
            break
    print('#{} {}'.format(tc, ans))
