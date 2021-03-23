
'''
https://programmers.co.kr/learn/courses/30/lessons/42577

'''


'''
list 를 돌면서 첫번째 타겟 인자 구함
다른 항목들을 타겟 길이만큼만 계속 비교
같은게 없으면 true
같은게 있으면 false
'''


def solution2(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            return False

    return True


def solution(phoneBook):
    import re
    for b in phoneBook:
        p = re.compile("^"+b)
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True


print("답 : ", solution(["119", "97674223", "1195524421"]))  # false
print("답 : ", solution(["123", "456", "789"]))  # true
print("답 : ", solution(["12", "123", "1235", "567", "88"]))  # false
