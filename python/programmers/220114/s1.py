# 미해결
# 소요시간 25분

def solution(citations):
    answer = 0
    
    temp = sorted(citations, reverse=True)
    i = 0
    print(temp)
    while True:
        # 내림 차순으로 정렬된 리스트의 가장 큰 원소값을 기준으로 시작.
        # 해당 원소 값이, idx 0 ~ i 까지 길이보다 같거나 작고, idx i ~ -1 까지 보다 크면 H-index
        if len(temp[0:i])+1 >= temp[i] and len(temp[i:]) <= temp[i]:
            answer = temp[i]
            break
        # H-index가 아니면 한칸 뒤로 가서 확인
        # 앞으로 갈 필요 x
        else:
            i += 1
    
    return answer

print(solution([10, 8, 5, 4, 3]))