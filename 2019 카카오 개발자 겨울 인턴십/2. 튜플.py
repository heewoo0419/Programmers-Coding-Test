def solution(s):
    answer = []
    lists = s[2:-2].split("},{")
    lists.sort(key=len)
    for li in lists:
        numbers = list(map(int, li.split(",")))
        for num in numbers:
            if num not in answer:
                answer.append(num)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))        # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))        # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))                     # [111, 20]
print(solution("{{123}}"))                              # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))        # [3, 2, 4, 1]
