from itertools import permutations

def go(x):
    global wow
    temp = int(''.join(x).lstrip('0'))
    if temp < 2: 
        return False 
    for i in range(2, temp): 
        if temp % i == 0: # 이 조건이 이해가 안감  참고 : https://53perc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84%ED%95%98%EA%B8%B0
            return False 
    if temp in wow:
        return False
    wow.append(temp)
    
def solution(numbers):
    for i in range(1, len(numbers)+1):
        # 1. 순열 구하고
        perms = permutations(numbers, i)
        # 2. 각 순열 마다 소수인지 확인
        list(filter(go, perms))
    # 3. 구한 소수의 개수만큼 정답
    return len(wow)

wow = []