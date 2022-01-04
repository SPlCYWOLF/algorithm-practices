# 13 / 15 통과

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
    for k in total:
        cnt = 0
        for candidate in rough:
            if cnt == 2:
                break
            if candidate[1] == k[0]:
                cnt += 1
                answer.append(candidate[2])
    # print(answer)
    return answer
