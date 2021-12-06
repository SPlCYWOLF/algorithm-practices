import sys
sys.stdin = open('input.txt', encoding='UTF-8')


for _ in range(1, 11):
    
    tc = int(input())
    target = input()
    letters = input()

    t = len(target)
    l = len(letters)
    
    i, j, cnt= 0, 0, 0
    
    while j < l and i < t:
        if target[i] == letters[j]:
            j += 1
            i += 1
        else:
            j = j - i + 1
            i = 0
        if i == t:
            cnt += 1
            i = 0
    
    print('#{} {}'.format(tc, cnt))