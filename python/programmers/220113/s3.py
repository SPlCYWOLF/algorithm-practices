# 프로그래머스 다른 사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# any ->
# Return True if any element of the iterable is true. If the iterable is empty, return False.
# 구조:
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False