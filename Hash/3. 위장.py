def solution(clothes):
    category = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in category:
            category[cloth[1]] += 1
        else:
            category[cloth[1]] = 1

    for value in category.values():
        answer *= (value+1)

    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))