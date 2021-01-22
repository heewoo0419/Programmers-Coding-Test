import sys
sys.setrecursionlimit(2000)


# 효율성 수정 코드
def solution(k, room_number):

    def find_empty_room(r_n, rooms):
        if r_n not in rooms:
            rooms[r_n] = r_n + 1
            return r_n
        find = find_empty_room(rooms[r_n], rooms)
        rooms[r_n] = find + 1
        return find

    answer = []
    rooms = dict()
    for r_n in room_number:
        empty = find_empty_room(r_n,rooms)
        answer.append(empty)
    return answer


# 효율성 실패 코드
def fail_solution(k, room_number):
    room_dict = dict()
    answer = []
    while room_number:
        r_n = room_number.pop(0)
        while True:
            if r_n not in answer:
                answer.append(r_n)
                break
            else:
                r_n += 1
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))  # [1,3,4,2,5,6]
