import math

def solution(progresses, speeds):
    answer = []
    temp = []
    
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        temp.append(days)

    i, j, cnt = 0, 0, 0
    while j <= len(temp)-1:
        if temp[j] <= temp[i]:
            cnt += 1
            j += 1
        else:
            answer.append(cnt)
            i = j
            cnt = 0
            
    answer.append(cnt)
                
    return answer