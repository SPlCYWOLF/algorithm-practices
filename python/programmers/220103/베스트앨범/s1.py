def solution(genres, plays):
    # 장르와 재생횟수를 딕셔너리로 생성
    # 장르별 총 재생횟수를 확인하고 그 장르 순서를 새로운 리스트에 기록
    # 장르 순서 루프를 돌고, 2중 루프로 딕셔너리 길이만큼 루프를 돌며 해당 장르의 max값을 확인
    # 해당 max값의 index를 plays리스트에서 찾아서 answer 리스트에 할당
    hua = []
    answer = {}
    temp = list(zip(genres, plays))
    print(temp)

    for i in range(len(temp)):
        if temp[i][0] in answer:
            answer[temp[i][0]] += temp[i][1]
        else:
            answer[temp[i][0]] = temp[i][1]
    print(answer)
    wow = sorted(answer.keys(), reverse=True)
    ho = sorted(temp, reverse=True)
    print(wow)
    print(ho)
    
    for i in range(len(temp)):
        pass
    
# 미완성
        