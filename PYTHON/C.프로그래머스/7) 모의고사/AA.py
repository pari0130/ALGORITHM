'''
프로그래머스 모의고사 문제

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

'''
import sys
answers = [1, 2, 3, 4, 5]  # [1,3,2,4,2] [1, 2, 3, 4, 5] [2, 1, 3, 4, 4]
supo_a = [1, 2, 3, 4, 5]  # len 5
supo_b = [2, 1, 2, 3, 2, 4, 2, 5]  # len 8
supo_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # len 10


'''
1. 정답을 돌면서
2. 정답 index와 답안 index 를 비교해서 맞을 경우 cnt += 1
3. 3명 체크 후
'''


def solution(answers):
    answer = []
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    for i in range(len(answers)):
        if answers[i] == supo_a[(i % len(supo_a))]:
            cnt_a += 1
        if answers[i] == supo_b[(i % len(supo_b))]:
            cnt_b += 1
        if answers[i] == supo_c[(i % len(supo_c))]:
            cnt_c += 1

    answer_temp = [cnt_a, cnt_b, cnt_c]

    for person, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person + 1)

    # tmp_answer = [(1, cnt_a), (2, cnt_b), (3, cnt_c)]
    # tmp_answer.sort(key=lambda x: x[1])

    # for val in tmp_answer:
    #     if val[1] != 0:
    #         answer.append(val[0])

    print(answer)

    return answer


solution(answers)
