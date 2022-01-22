from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        temp = list(permutations(numbers, i+1))
        print(temp)
        for num in temp:
            temp2 = ''.join(num).lstrip('0')
            # 여기서 temp2 를 정수로 변환하여 실수 여부를 판단하고 asnwer에 중복 없이 넣으면, 총 answer 길이가 정답
            # 하지만 정수로 변환이 안됨. 어이없음.
            print(temp2)
            # if int(temp2)%2 and int(temp2)%3 and int(temp2.lstrip(0)) != 1 and temp2 not in answer:
            #     answer.append(temp2)
        
    return answer