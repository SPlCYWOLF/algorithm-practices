# 패작
def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = []
    Q.append(truck_weights.pop(0))

    while truck_weights:
        # 일단 bridge_length 랑 weight 조건 내로 temp에 다 채워넣고   answer -= 1
            
        # temp 길이 1 이상이면 앞에거 하나씩 temp로 이동하고   answer += weight

        # temp 길이 1 이면 Q로 옮기고    answer += weight

    # 마지막으로 answer += 남은 길이 + len(temp)

    return answer
                                                        
print('#1. {}'.format(solution(3, 15, [10, 4, 5, 3, 10]))) # 답 : 10
print('#2. {}'.format(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))) # 답 : 110
print('#3. {}'.format(solution(2, 10, [7,4,5,6])))  # 답 : 8