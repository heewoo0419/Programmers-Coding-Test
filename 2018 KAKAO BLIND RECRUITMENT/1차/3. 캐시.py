def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        # 소문자 변경
        city = city.lower()
        # 캐시 적중 시
        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

        # 캐시 적중 실패 시
        else:
            answer += 5
            # 캐시가 충분하면
            if len(cache) < cacheSize:
                cache.append(city)
            # 캐시 부족 시
            else:
                # 캐시 사이즈가 0 이상일 때
                if cacheSize > 0:
                    cache.pop(0)
                    cache.append(city)
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork","Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork","Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
