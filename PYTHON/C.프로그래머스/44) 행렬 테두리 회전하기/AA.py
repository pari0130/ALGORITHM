'''
https://school.programmers.co.kr/learn/courses/30/lessons/77485

x1, y1, x2, y2 정수 4개
x1행 y1열부터 x2행y2열 까지 영역의 숫자를 시계 방향으로 회전

'''
from collections import deque


def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1]  # 회전 배열의 첫번쨰 값 저장, 마지막에 append 용 e.g. 8
        mini = tmp

        for k in range(x1 - 1, x2 - 1):  # 왼쪽 세로, 열고정 행감소 하면서 변경
            test = array[k + 1][y1 - 1]  # 3행 2열의 값을
            array[k][y1 - 1] = test  # 2행 2열로 옮김
            mini = min(mini, test)  # 최소값 비교

        for k in range(y1 - 1, y2 - 1):  # 하단 가로, 행고정 열감소 하면서 변경
            test = array[x2 - 1][k + 1]
            array[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):  # 오른쪽 세로
            test = array[k - 1][y2 - 1]
            array[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):  # 상단 가로
            test = array[x1 - 1][k - 1]
            array[x1 - 1][k] = test
            mini = min(mini, test)

        array[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer


print("답 : ", solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))  # [8, 10, 25]
print("답 : ", solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))  # [1, 1, 5, 3]
print("답 : ", solution(100, 97, [[1, 1, 100, 97]]))  # [1]


# 로테이트 활용
def solution2(rows, columns, queries):
    arr = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a, b, c, d = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
        for x in range(d - b):
            answer.append(arr[a][b + x])
        for y in range(c - a):
            answer.append(arr[a + y][d])
        for z in range(d - b):
            answer.append(arr[c][d - z])
        for k in range(c - a):
            answer.append(arr[c - k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d - b):
            arr[a][b + x] = answer[0]
            answer.popleft()
        for y in range(c - a):
            arr[a + y][d] = answer[0]
            answer.popleft()
        for z in range(d - b):
            arr[c][d - z] = answer[0]
            answer.popleft()
        for k in range(c - a):
            arr[c - k][b] = answer[0]
            answer.popleft()
    return result
