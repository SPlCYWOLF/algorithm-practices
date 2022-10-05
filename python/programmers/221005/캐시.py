from collections import deque
import sys

sys.stdin = open('input.txt')


cacheSize = int(input())
cities = list(input().split())

answer = 0
cache = deque()

if cacheSize:
    for city in cities:
        city = city.lower()

        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)

            answer += 5

        else:
            cache.remove(city)  # 한번 사용되면 최근사용했다고 반영
            cache.append(city)
            answer += 1
else:
    answer += len(cities) * 5

print(answer)