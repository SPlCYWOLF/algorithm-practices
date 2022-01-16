# 문제 이해에 시간이 걸렸던 문제.

def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                cnt += 1
            # s1.py 에서, 1초 경과의 기준을 명확하게 해주니 문제 해결 
            elif prices[j] < prices[i]:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    
    return answer