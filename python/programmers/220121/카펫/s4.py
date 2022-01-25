# 성공..!!

def solution(brown, yellow):
    temp = brown + yellow
    yaksu = []
    for i in range(1, temp+1):
        if temp % i == 0:
            yaksu.append(i)
    
    mid = len(yaksu) // 2
    L = len(yaksu)
    if len(yaksu) % 2:
        for i in range(mid+1):
            if (yaksu[i] * 2) + (yaksu[L-i-1] * 2) - 4 == brown:
                return [yaksu[L-i-1], yaksu[i]]
    else:
        for i in range(mid):
            if (yaksu[i] * 2) + (yaksu[L-i-1] * 2) - 4 == brown:
                return [yaksu[L-i-1], yaksu[i]]