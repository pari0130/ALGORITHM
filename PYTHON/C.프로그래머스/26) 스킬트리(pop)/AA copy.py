
'''
'''


def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        idx = 0
        tmp_skill = list(skill)
        # tmp_skill = []
        # tmp_skill = [j for j in i if j in skill]
        print(tmp_skill)

        for j in i:
            if j in skill:
                if j != tmp_skill.pop(0):
                    answer += 1
                    break

        '''
        포함되는 값을 뽑아와서 
        '''

        # tmp_skill = ""
        # # cur[1]가 가장 큰수가 아닐 경우
        # if any(tmp_skill += j for j in i if j in skill):
        #     queue.append(cur)

        # for j in i:
        #     if j not in skill:
        #         continue
        #     else:
        #         tmp_skill += j

    return answer


# print("답 : ", solution("CBD", ["BACDE"]))  # 2
print("답 : ", solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
