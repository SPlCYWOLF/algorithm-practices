from itertools import permutations

def go(x):
    global wow
    if int(''.join(x)) % 2 and int(''.join(x)) % 3 and int(''.join(x)) != 1:
        # print(''.join(x))
        if ''.join(x).lstrip('0') not in wow:
            wow.append(''.join(x).lstrip('0'))

def solution(numbers):
    for i in range(1, len(numbers)+1):
        # 1. 순열 구하고
        perms = permutations(numbers, i)
        # 2. 각 순열 마다 소수인지 확인
        list(filter(go, perms))
    # 3. 구한 소수의 개수만큼 정답
    answer = len(wow)
    
    return answer

wow = []