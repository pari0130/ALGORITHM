
'''
방법만 생각해서 맞는지 정답 비교

** 한개의 문자가 얼마나 반복 되는지 == 1개 단위로 자른다 의미임

알고리즘

1. 만약 input된 문자열의 길이가 1이라면 1을 return한다.
2. 자를 길이를 1부터 (문자열 길이 나누기 2한 몫) + 1까지 for문을 돌린다.(절반 이상까지 자르는 것은 무의미하다.)
3. count = 1로 초기화하고, 임시저장 str을 처음부터 자를 길이까지 잘라 저장한다.
4. for i in range(cut,len(s), cut) => range의 3번째 항에 cut을 넣으면 자를 단위 만큼 건너뛰며 for문을 돈다.
5. tempStr에 저장한 이후의 문자열이 cut 단위로 자른 문자 s[i:i+cut] 와 같다면 count에 1을 더해준다.
6. 같지 않고 count == 1이라면 count ="" 로 셋팅하고, count !=1이라면 result = result + str(count) + tempStr을 해준다.
7. 다시 tempStr에 s[i:i+cut] 을 저장하고( s[i:i+cut]이 이전 tempStr과 달랐기 때문에 현재 tempStr로 셋팅), count =1로 초기화 한다.
8. Length 중 최소값을 return한다.
'''


def solution(s):
    length = []
    result = ""

    # 1. 만약 input된 문자열의 길이가 1이라면 1을 return한다.
    if len(s) == 1:
        return 1

    # 2. 자를 길이를 1부터(문자열 길이 나누기 2한 몫) + 1까지 for문을 돌린다.(절반 이상까지 자르는 것은 무의미하다.)
    for cut in range(1, len(s) // 2 + 1):

        # 3. count = 1로 초기화하고, 임시저장 str을 처음부터 자를 길이까지 잘라 저장한다.
        count = 1
        tempStr = s[:cut]
        print(tempStr)

        # 4. for i in range(cut,len(s), cut) => range의 3번째 항에 cut을 넣으면 자를 단위 만큼 건너뛰며 for문을 돈다.
        for i in range(cut, len(s), cut):

            # 5. tempStr에 저장한 이후의 문자열이 cut 단위로 자른 문자 s[i:i+cut] 와 같다면 count에 1을 더해준다.
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                # 6. 같지 않고 count == 1이라면 count ="" 로 셋팅하고, count !=1이라면 result = result + str(count) + tempStr을 해준다.
                if count == 1:
                    count = ""
                result += str(count) + tempStr

                # 7. 다시 tempStr에 s[i:i+cut] 을 저장하고( s[i:i+cut]이 이전 tempStr과 달랐기 때문에 현재 tempStr로 셋팅), count =1로 초기화 한다.
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    # 8. Length 중 최소값을 return한다.
    return min(length)


print(solution("aabbaccc"))  # 2a2ba3c -> result 7 1개단위로 자를 경우 가장 짧음
# print(solution("ababcdcdababcdcd"))  # 2ababcdcd -> result 9 8개단위로 자를 경우 가장 짧음
# print(solution("abcabcdede"))  # 8
# print(solution("abcabcabcabcdededededede"))  # 14
# print(solution("xababcdcdababcdcd"))  # x문자열이 있어서 중복되는 문자가 없기에 제일 짧은게 17
