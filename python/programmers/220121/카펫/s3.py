def solution(brown, yellow):
    # 실패작
    temp = brown + yellow
    yaksu = []
    for i in range(1, temp+1):
        if temp % i == 0:
            yaksu.append(i)

    mid = len(yaksu) // 2      
    if len(yaksu) % 2:
        for f in yaksu[:mid+1]:
            for b in yaksu[mid::-1]:
                if (f * 2) + (b * 2) - 4 == brown:
                    return [b, f]
    else:
        for f in yaksu[:mid]:
            for b in yaksu[mid::-1]:
                if (f * 2) + (b * 2) - 4 == brown:
                    return [b, f]

