'''
https://school.programmers.co.kr/learn/courses/30/lessons/135808

k 가 최상위 점수, 1점이 최하품
m 개씩 한상자 담음

'''


def solution(k, m, score):
    answer = 0
    score.sort()  # 오름차순 정렬

    while True:
        if len(score) < m:
            break
        b = []
        for i in range(m):
            b.append(score.pop())
        b.sort()
        answer += (b[0] * m)

    return answer


print("답 : ", solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))  # 8
print("답 : ", solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))  # 8
