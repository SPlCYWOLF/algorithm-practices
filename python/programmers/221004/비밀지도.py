import sys
sys.stdin = open('input.txt')

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer = []
for i in range(n):
    map1, map2 = "{0:b}".format(arr1[i]), "{0:b}".format(arr2[i])
    L1, L2 = len(map1), len(map2)

    if L1 < n:
        map1 = '0' * (n - L1) + map1
    if L2 < n:
        map2 = '0' * (n - L2) + map2

    final_map = ""
    for j in range(n):
        if map1[j] == '0' and map2[j] == '0':
            final_map += ' '
        else:
            final_map += '#'

    answer.append(final_map)

print(answer)