def solution(s):
    compressed_list = [len(s)]
    for size in range(1, len(s)):
        split = [s[i:i+size] for i in range(0, len(s), size)]
        count = 1
        temp = split[0]
        string = ""

        for word in split[1:]:
            if temp == word:
                count += 1
            else:
                string += (str(count) + temp) if count > 1 else temp
                temp = word
                count = 1
        string += (str(count) + temp) if count > 1 else temp
        compressed_list.append(len(string))

    return min(compressed_list)


print(solution("a"))
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
