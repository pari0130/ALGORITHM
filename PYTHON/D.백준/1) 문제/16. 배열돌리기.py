'''
https://www.acmicpc.net/problem/16926

반시계 방향 회전

테두리 list 조회 -> q -> rotate -> append
'''
from collections import deque

n, m, r = map(int, input().split())  # 행 열 회전수
a = [list(map(int, input().split())) for _ in range(n)]  # 배열
rotate_q = deque()
rotate = []


def board_rotate_and_insert(j, type):
    # 행증가
    for x in range(j, n - j):
        if type == 1:
            rotate_q.append(a[x][j])
        else:
            a[x][j] = rotate_q.popleft()

    # 열증가
    for y in range(j + 1, m - j, 1):
        if type == 1:
            rotate_q.append(a[m - j - 1][y])
        else:
            a[m - j - 1][y] = rotate_q.popleft()

    # 열고정 행감소
    for z in range(m - j - 1, j, -1):
        if type == 1:
            rotate_q.append(a[z - 1][m - j - 1])
        else:
            a[z - 1][m - j - 1] = rotate_q.popleft()

    # 행고정 열감소
    for k in range(m - j - 1, j + 1, -1):
        if type == 1:
            rotate_q.append(a[j][k - 1])
        else:
            a[j][k - 1] = rotate_q.popleft()

    if type == 1:
        rotate_q.rotate()

    return rotate_q


for i in range(r):
    for j in range(n // 2):
        rotate_q.clear()
        board_rotate_and_insert(j, 1)  # rotate
        board_rotate_and_insert(j, 2)  # add


for i in range(n):
    for j in range(m):
        print(rotate_q[i][j], end=' ')
    print()


# 시간초과 함.....