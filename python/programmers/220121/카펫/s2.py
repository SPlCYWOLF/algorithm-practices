# 정답이지만 참고도 못할 정도로 수학적인 풀이
import math

def solution(brown, yellow):
    num = int(math.sqrt(yellow))
    
    for i in range(1, num+1):
        if yellow % i == 0:
            a = i
            b = yellow // i
            if (a+2)*(b+2) == brown + yellow:
                break
        
    return [b+2, a+2]