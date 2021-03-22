
'''
'''


def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        tmp_skill = list(skill)
        print(tmp_skill)

        # for-else 문의 경우 break 가 발생하지 않았을 경우 for 문 이후 else 를 타게 된다.
        # 쉽게 break - else 문
        for j in i:
            if j in skill:
                if j != tmp_skill.pop(0):
                    break
        else:
            answer += 1

    return answer


# print("답 : ", solution("CBD", ["BACDE"]))  # 2
print("답 : ", solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
