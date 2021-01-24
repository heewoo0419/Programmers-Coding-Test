# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
def solution(N, stages):
    stage_dict = {}
    clear = len(stages)

    for i in range(1, N+1):
        if clear != 0:
            no_clear = stages.count(i)
            stage_dict[i] = no_clear/clear
            clear -= no_clear
        else:
            stage_dict[i] = 0

    answer = sorted(stage_dict, key=lambda x: stage_dict[x], reverse=True)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# [3,4,2,1,5]

print(solution(4, [4, 4, 4, 4, 4]))
# [4,1,2,3]