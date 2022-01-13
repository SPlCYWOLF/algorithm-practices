# 패작

def solution(priorities, location):
    answer = 1
    Q = []

    for idx, num in enumerate(priorities):
        Q.append((idx, num))
    
    i = 0
    while len(Q):
        max_num = max(Q, key=lambda x:x[1])
        if Q[i][1] == max_num[1]:
            if Q[i][0] == location:
                break
            else:
                Q.pop(i)
                answer += 1
        if i >= len(Q)-1:
            i = 0
        else:
            i += 1

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))