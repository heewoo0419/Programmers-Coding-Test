import re
def solution(record):
    answer = []
    lists = []
    user_dict = {}

    for r in record:
        if 'Leave' in r:
            status, uid = r.split(" ")
            lists.append([status, uid])
        elif 'Change' in r:
            status, uid, name = r.split(" ")
            user_dict[uid] = name
        else:
            status, uid, name = r.split(" ")
            user_dict[uid] = name
            lists.append([status, uid])

    for status, uid in lists:
        if status == "Enter":
            answer.append(user_dict[uid]+"님이 들어왔습니다.")
        else:
            answer.append(user_dict[uid] + "님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]