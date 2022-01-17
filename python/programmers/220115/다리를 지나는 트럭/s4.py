def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = []
    truck_weights = sorted(truck_weights, reverse=True)
    Q.append(truck_weights.pop(0))
    while truck_weights:
        # weight 보다 작고 bridge_length 보다 짧으면 Q에 차를 더 실음
        if (sum(Q) + truck_weights[0]) <= weight and len(Q) < bridge_length:
            Q.append(truck_weights.pop(0))
        # 아니면 스탑하고 (Q + 다리 길이) 만큼 answer에 더해줌
        else:
            answer += len(Q) + bridge_length
            # 다리가 비워지는 순간 차량이 하나 올라오니, 그만큼 시간을 1 빼줌
            Q = [truck_weights.pop(0)]
            answer -= 1
    
    answer += len(Q) + bridge_length
    return answer

print('#1. {}'.format(solution(3, 15, [10, 4, 5, 3, 10]))) # 답 : 11
print('#2. {}'.format(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))) # 답 : 110
print('#3. {}'.format(solution(2, 10, [7,4,5,6])))  # 답 : 101