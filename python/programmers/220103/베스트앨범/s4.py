def solution(genres, plays):

    answer = []
    # 장르 표시 & 재생+idx 딕셔너리 생성
    G, S = {}, {}

    for i in range(len(genres)):
        G[genres[i]] = G.get(genres[i], 0) + plays[i]
        S[genres[i]] = S.get(genres[i], []) + [(plays[i], i)]
    # 장르별 높은 재생횟수 순으로 sort된 장르 리스트 생성
    # 질문: lambda x:x[0] 이라 하면 왜 틀리지
    genre_ordered = sorted(G.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in genre_ordered:
        # 재생 수 오름차순, idx 내림차순으로 정렬된 리스트 중 2개 요소만 리스트로 생성
        play_idx_ordered = sorted(S[genre], key=lambda x: (-x[0], x[1]))[:2]
        # idx 만 차례대로 answer에 append
        for song in play_idx_ordered:
            answer.append(song[1])

    return answer
