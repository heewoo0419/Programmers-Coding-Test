def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        answer.append(format(a1 | a2, 'b').zfill(n).replace("1", "#").replace("0", " "))
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))