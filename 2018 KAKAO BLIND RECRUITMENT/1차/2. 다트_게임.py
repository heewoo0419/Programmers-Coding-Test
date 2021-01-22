import re
import math


def solution(dartResult):
    answer = 0
    stack = []
    result = re.findall('(\d+)([SDT])([*#]?)', dartResult)

    for score, bonus, option in result:
        s = 0
        if bonus == 'S':
            s += int(score)
        elif bonus == 'D':
            s += int(math.pow(int(score), 2))
        elif bonus == 'T':
            s += int(math.pow(int(score), 3))

        if option == "*":
            if len(stack) > 0:
                before = stack.pop()
                before *= 2
                stack.append(before)
            s *= 2

        elif option == "#":
            s = -s
        stack.append(s)
    answer = sum(stack)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1S*2T*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
