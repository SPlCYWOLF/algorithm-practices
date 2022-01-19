def solution(answers):
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            cnt1 += 1
        if answers[i] == p2[i]:
            cnt2 += 1
        if answers[i] == p3[i]:
            cnt3 += 1
            
    temp = {1: cnt1, 2: cnt2, 3: cnt3}
    top = max(temp.values())
    answer = [s for s, num in temp.items() if num == top]
    
    return answer