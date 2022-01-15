# 패작 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 최대 깊이로 넣고 더이상 안들어가면 다리 길이만큼 더하고 큐 길이만큼 더하고 반복
    Q = []
    daegi = deque(sorted(truck_weights, reverse=True))
    
    while daegi:
        
        if len(Q) < bridge_length and sum(Q)+daegi[0] < weight:
            Q.append(daegi.popleft())
            if len(daegi) == 0:
                answer += len(Q)

        else:
            answer += bridge_length + len(Q)
            Q = []
    
    return answer