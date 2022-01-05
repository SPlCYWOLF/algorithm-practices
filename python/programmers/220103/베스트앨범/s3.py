def solution(genres, plays):

    answer = []

    # 딕셔너리를 만들어서 해당 장르별로 가장 많은 재생횟수 별로 sort된 장르 리스트 생성
    total = {}
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
        else:
            total[genres[i]] = plays[i]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    # 장르와 플레이를 2중 리스트로 각각 묶기 ([재생횟수, 장르, idx])
    temp = list(zip(plays, genres, range(len(genres))))
    # 2중 리스트 재생횟수 별로 sort
    rough = sorted(temp, reverse=True)
    # print(rough)
    # print(total)
    # sort된 장르 리스트 순서로 2중 리스트를 돌며 answer에 할당

    temp = []
    for k in total:
        cnt = 0
        for candidate in rough:
            if cnt == 2:
                break
            if candidate[1] == k[0]:
                cnt += 1
                temp.append(candidate)
    print(temp)
    # 같은 장르고, 재생횟수가 동일하고, 앞&뒤 중 앞 요소의 인덱스 번호가 더 크면 위치 change
    for i in range(len(temp)-1):
        if temp[i][1] == temp[i+1][1] and temp[i][0] == temp[i+1][0] and temp[i][2] > temp[i+1][2]:
            temp[i], temp[i+1] = temp[i+1], temp[i]

    # temp 돌면서 두개의 장르를 담으면 == answer 완성 (break로 append 중단)
    cnt = 0
    for i in range(len(temp)):
        if cnt == 2:
            break
        if i < len(temp)-1 and temp[i][1] != temp[i+1][1]:
            cnt += 1
        answer.append(temp[i][2])

    return answer

    # 문제점 : 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    # 위 문제점은 해결. 하지만 또다른 문제점이 생겨서 실패. 화나네 아.
