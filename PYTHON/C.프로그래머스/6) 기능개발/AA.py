'''
프로그래머스 기능개발 문제

'''
import sys
import math
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []
    ans_list = []

    # 1. math.ceil() 로 몫을 구함
    for i in range(len(progresses)):
        ans_list.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # 2. 몫 을 ans_list 에 저장
    while True:
        if len(ans_list) == 0:
            break

        target = ans_list.pop(0)
        cnt = 1

        # 3. 타겟을 pop 한뒤 길이가 0일 경우 타겟에 해당하는 카운트는 1
        if len(ans_list) == 0:
            answer.append(cnt)
        else:
            # 4. 그렇지 않을 경우 답 list를 돌면서 타겟보다 작은 값을 tmp_list에 담은 뒤 길이를 answer에 저장
            for i in range(len(ans_list)):
                if ans_list[0] > target:
                    break
                else:
                    cnt += 1
                    ans_list.pop(0)
            answer.append(cnt)

    print(answer)

    return answer


solution(progresses, speeds)
