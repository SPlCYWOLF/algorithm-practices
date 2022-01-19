# 참고: https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC

def solution(answers):
    first_st = [1,2,3,4,5]
    second_st = [2,1,2,3,2,4,2,5]
    third_st = [3,3,1,1,2,2,4,4,5,5]
    first_count = 0
    second_count= 0
    third_count = 0
    for index, answer in enumerate(answers):
        if answer == first_st[index%5]:
            first_count+=1
        if answer == second_st[index%8]:
            second_count+=1
        if answer == third_st[index%10]:
            third_count +=1
    count_dict = {1: first_count, 2:second_count, 3:third_count}
    top_score = max(count_dict.values())
    result = [student for student,score in count_dict.items() if score==top_score]
            
    return result