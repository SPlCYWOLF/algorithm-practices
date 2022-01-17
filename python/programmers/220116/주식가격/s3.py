# 다른분 풀이.
# 인덱스 처리가 매우 깔끔하다.
# 특히, append를 처리 할 필요없이 해당 인덱스 원소값을 더하는게 인상 깊음
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer