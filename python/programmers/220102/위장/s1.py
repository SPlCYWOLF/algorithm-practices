## 패작

# def comb(clothes, status, k):
#     global omg
#     for i in range(k, len(clothes)):
#         if clothes[i][1] not in status:
#             status[k] = clothes[i][1]
#             print(status)
#             omg.append(status)
#             comb(clothes, status, k+1)
#             status[k] = 0
    
            
# def solution(clothes):
#     answer = 0
#     temp = []
#     for cloth in clothes:
#         if cloth[1] not in temp:
#             temp.append(cloth[1])
    
#     temp2 = [0] * len(temp)
#     comb(clothes, temp2, 0)
#     # temp3 = set(tuple(omg) for i in omg)
#     answer = omg
#     return answer

# omg = []
    

def solution(clothes):
    answer = {}
    for cloth in clothes:
        if cloth[1] in answer:
            answer[cloth[1]] += 1
        else:
            answer[cloth[1]] = 1
    print(answer)
    
    cnt = 1
    # 이 부분은 도저히 이해가 안간다
    for value in answer.values():
        cnt *= (value+1)
    return cnt - 1
