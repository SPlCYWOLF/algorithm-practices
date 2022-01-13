def solution(priorities, location):
    answer = 0
    temp = []
    # 1. 우선순위와 해당 프린트물의 idx를 하나로 묶기
    for idx, num in enumerate(priorities):
        temp.append((idx, num))
    
    done = []
    i = 0
    while True:
        max_num = max(temp, key=lambda x:x[1])
        # 2. 프린트 큐 내의 가장 큰 수 인지 확인
        if temp[i][1] == max_num[1]:
            # 3. 프린트하면 done 에 기록
            done.append(temp.pop(i))
            # 4. pop 해주었으니 그만큼 i 하나 줄여줌
            i -= 1
            # 5. 프린트 한것이 원하는 프린트물인지 확인
            if done[-1][0] == location:
                # 6. 원하는 프린트 물이면, 몇번째로 프린트 되었는지 반환
                answer = len(done)
                break
        # 5-5. 원하는 프린트물이 아니면 다시 원활한 프린트물 검색위해 i 값 조정
        if i >= len(temp)-1:
            i = 0
        else:
            i += 1
        
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))