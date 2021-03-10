
'''
방법만 생각해서 맞는지 정답 비교

** 한개의 문자가 얼마나 반복 되는지 == 1개 단위로 자른다 의미임
'''


def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)


print(solution("aabbaccc"))  # 2a2ba3c -> result 7 1개단위로 자를 경우 가장 짧음
# print(solution("ababcdcdababcdcd"))  # 2ababcdcd -> result 9 8개단위로 자를 경우 가장 짧음
# print(solution("abcabcdede"))  # 8
# print(solution("abcabcabcabcdededededede"))  # 14
# print(solution("xababcdcdababcdcd"))  # x문자열이 있어서 중복되는 문자가 없기에 제일 짧은게 17
