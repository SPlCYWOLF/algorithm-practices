# 패작2

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)-i):
            temp = numbers[j:j+i+1].lstrip('0')
            if temp not in answer and temp and (int(temp)%2 and int(temp)%3) and temp != '1':
                answer.append(temp)
            temp2 = ''.join(reversed(temp))
            if temp2 not in answer and temp2 and (int(temp2)%2 and int(temp2)%3) and temp2 != '1':
                answer.append(temp2)
            print(temp2, temp)   
            print(answer)
    return len(answer)