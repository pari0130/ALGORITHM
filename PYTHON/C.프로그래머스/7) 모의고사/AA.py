'''
프로그래머스 모의고사 문제

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

'''
import sys
answers = [1, 2, 3, 4, 5]
supo_a = [1, 2, 3, 4, 5]  # len 5
supo_b = [2, 1, 2, 3, 2, 4, 2, 5]  # len 8
supo_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # len 10

# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
#             return [(p % n)+1, (p//n)+1]
#     else:
#         return [0, 0]
'''
1. 정답을 담을 tuple list [(1,3), (2,5), (3,1)]
2. 각 list 길이와 정답 길이의 최소 공배수 구함
3. 최소 공배수 만큼만 loop 하여 정답 카운트
4. 튜플 형태 정렬 v.sort(key=lambda x:-x[1])
5. 튜플 형태 x[0] 의 값을 answer 출력 -> 0의 값이 1,2,3 학생의 번호값 1의 값이 1,2,3 학생의 맞힌 개수
'''


def GCD(X, Y):  # 최대공약
    while(Y):
        X, Y = Y, X % Y
    return X


def LCM(X, Y):  # 최소공배
    result = (X*Y) // GCD(X, Y)
    return result


def result(answers, supo_list, num):
    cnt_a = 0
    for i in range(LCM(len(answers), len(supo_list))):
        if supo_list[(i % len(supo_list))] == answers[(i % len(answers))]:
            cnt_a += 1
    # tp = (num, cnt_a * (max / len(supo_list)))
    tp = (num, cnt_a)
    return tp


def solution(answers):
    global max
    max = 10000
    answer = []
    tp_answer = []  # 정답 tuple

    tp_answer.append(result(answers, supo_a, 1))
    tp_answer.append(result(answers, supo_b, 2))
    tp_answer.append(result(answers, supo_c, 3))

    print(tp_answer)
    return answer


# print(LCM(2, 6))

solution(answers)
