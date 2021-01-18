def solution(phone_book):
    answer = True
    phone_book.sort(key = len)
    for phone in phone_book[1:]:
        if str(phone_book[0]) in str(phone[:len(phone_book[0])]):
            answer = False
            break
    return answer