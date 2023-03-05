'''
https://school.programmers.co.kr/learn/courses/30/lessons/135807
'''
import numpy as np

def solution(arrayA, arrayB):
    answer = 0
    gcdA = int(np.gcd.reduce(arrayA))
    gcdB = int(np.gcd.reduce(arrayB))
    answerA = 0
    answerB = 0

    if gcdA > 1:
        for b in arrayB:
            if b > gcdA and b % gcdA == 0:
                answerA = 0
                break
            else:
                answerA = gcdA

    if gcdB > 1:
        print("22222")
        for a in arrayA:
            if a > gcdB and a % gcdB == 0:
                answerB = 0
                break
            else:
                answerB = gcdB

    if answerA > answerB:
        answer = answerA
    elif answerB > answerA:
        answer = answerB
    else:
        answer = 0

    return answer


print("답 : ", solution([10, 17], [5, 20]))  # 0
print("답 : ", solution([10, 20], [5, 17]))  # 10
print("답 : ", solution([14, 35, 119], [18, 30, 102]))  # 7
