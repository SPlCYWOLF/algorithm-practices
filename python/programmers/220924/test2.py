# Q.3
# 이모티콘 서비스 가입자를 최대한 늘리면서, 이모티콘 판매액 또한 최대로 늘렸을때,
# 서비스 가입자 수 & 판매액 정답으로 반환하라
# users = [[40, 10000], [25, 10000]], emoticons = [7000, 9000]
# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], emoticons = [1300, 1500, 1600, 4900]
# 정답 : [1, 5400]
# 정답 : [4, 13860]

# 이모티콘 구매 or 구매x -> 기준값 넘어가면 이모티콘 구매x -> 서비스 가입

# 확인사항 :
#   1. 이모티콘 별 할인율에 따른 최대 총 서비스 가입 & 구매 가격
#   2. 최대 전체 서비스 가입 & 구매 가격

# 각 이모티콘의 할인율마다 얼마나 많은 사람이 구매할지, 그리고 서비스 가입을 하게 될지 확인
# 개개인의 paid도 기록하여, 기준치를 넘기면 signup + 1 & revenue - paid
# 가장 많은 서비스 가입 및 많은 구매 가격을 기록

def solution(users, emoticons):
    total_max_rev = 0

    for emot in emoticons:
        max_signup, max_rev = 0, 0

        for i in range(1, 5):
            price = emot - (emot // 10) * i
            signup, rev = 0, 0

            for j in range(len(users)):
                user = users[j]
                discount, budget = user

                if i * 10 >= discount:
                    budget -= price
                    if budget

                        users[j][1] = budget
                    rev += price

    answer = []
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))







# Q.2
# 화물 배달 및 수거 완료까지 최단 이동 거리 구하라
# cap = 4, n = 5, deliveries = [1, 0, 3, 1, 2], pickups = [0, 3, 0, 4, 0]
# cap = 2, n = 7, deliveries = [1, 0, 2, 0, 1, 0, 2], pickups = [0, 2, 0, 1, 0, 2, 0]
# 정답 : 16
# 정답 : 30





# Q.1
# 오늘 날짜를 split 하여 dictionary에 년 월 일 별로 저장

# terms도 dictionary에 저장

# 각 privacy 마다 년 월 일 순으로 today의 dictionary와 대조

# 해당 privacy의 날짜는 term 만큼 갱신

# 만약 해당 privacy의 날짜가 년 월 일 순으로 today의 dictionary보다 크면,
# 파기로 간주

# def calculate_date(y, m, d, term):
#     if m + term > 12:
#         y += (m+term) // 12
#         m = (m + term) % 12
#     else:
#         m += term
#     return [y, m, d]
#
#
# def solution(today, terms, privacies):
#     answer = []
#
#     today = today.split(".")
#     today = {'year': int(today[0]), 'month': int(today[1]), 'day': int(today[2])}
#
#     term_dic = dict()
#     for term in terms:
#         term = term.split()
#         term_dic[term[0]] = int(term[1])
#
#     for privacy in privacies:
#         date, term = privacy.split()
#         y, m, d = date.split(".")
#         y, m, d = calculate_date(int(y), int(m), int(d), term_dic[term])
#
#         if y > today['year']:
#             continue
#         if y == today['year']:
#             if m > today['month']:
#                 continue
#             if m == today['month']:
#                 if d > today['day']:
#                     continue
#
#         answer.append(privacies.index(privacy)+1)
#
#     return answer
#
# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
