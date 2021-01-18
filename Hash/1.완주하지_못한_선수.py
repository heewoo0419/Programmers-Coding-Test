def solution(participant, completion):
    part_dict = {}
    for part in participant:
        if part in part_dict:
            part_dict[part] += 1
        else:
            part_dict[part] = 1

    for comp in completion:
        if comp in part_dict:
            part_dict[comp] -= 1
        if part_dict[comp] == 0:
            del part_dict[comp]

    answer = list(part_dict.keys())[0]
    return answer

