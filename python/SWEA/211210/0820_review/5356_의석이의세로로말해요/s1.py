import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):

    temp = [0] * 5
    max_len = 0

    for i in range(5):
        temp[i] = list(input())
        if len(temp[i]) > max_len:
            max_len = len(temp[i])
        
    print('#{}'.format(tc), end=' ')
    
    for i in range(max_len):
        for j in range(5):
            print()
            print(temp[j])
            if len(temp[j]) > i:    # why temp[i] 가 아닐까
                print(temp[j][i], end='')
    print()