
# 비트연산자 써야한다네 ㅎ 바로 포기
# 포인터 활용해 위치바꾸기

# 패작
# # 투자 시간 50분
# # anta tica (a n t i c) 애초에 K 가 5이상이 아니면 단어 한개도 못 가르킴
# # K 개의 글자로 읽을 수 없으는 단어는 배제
# # 단어 중복 제거 & 알파벳 정렬
# # .count() 해서 가장 높은 값이 정답

# import sys
# sys.stdin = open('input.txt')
#
# N, K = map(int, input().split())
# arr = [input() for _ in range(N)]
# rmv = ['a', 'n', 't', 'i', 'c']
# new_arr = []
# for word in arr:
#     for j in word:
#         if j in rmv:
#             word = word.replace(j, '0')
#     new_arr.append(word.strip('0'))
#
# print(arr)
# print(new_arr)