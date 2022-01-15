# 패작

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    daegi = sorted(truck_weights, reverse=True)
    dochak = []
    Q = []

    while daegi or Q:
        
        if len(Q) < bridge_length and sum(Q)+daegi[0] <= weight:
            Q.append(daegi.pop(0))
            answer += 1
            if len(daegi) != 0 and (weight <= sum(Q)+daegi[0] or len(Q) == bridge_length):
                answer += len(Q)
                Q = []
        if len(daegi) == 0:
            answer += len(Q)
            break
    
    return answer