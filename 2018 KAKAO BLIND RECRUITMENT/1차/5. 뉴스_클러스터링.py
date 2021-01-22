import re
from collections import Counter
import math

def solution(str1, str2):
    s1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
    s2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    c1 = Counter(s1)
    c2 = Counter(s2)

    # 중복 집합을 이용하기 위해 Count 합집합과 교집합 사용
    union = list((c1 | c2).elements())
    inter = list((c1 & c2).elements())

    if len(union) == 0:
        answer = 65536
    else:
        answer = math.trunc(65536 * (len(inter) / len(union)))

    return answer


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
