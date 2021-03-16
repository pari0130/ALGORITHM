
'''

'''
from collections import deque


# 현재 위치의 상하좌우 좌표 값 위치 구하기 위한 변수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(w, h):
    answer = 1
    n = w*h
    board = [[0] * w for _ in range(h)]
    dis = [[0] * w for _ in range(h)]  # dis 배열 8*16 길이 배열
    Q = deque()
    Q.append((0, 0))
    board[0][0] = 1  # 이동된 구간은 1로 초기화

    print(dis, end='\\n')

    while Q:
        tmp = Q.popleft()
        for i in range(4):  # 4방향 탐색
            # x = 기존 x 보다 커야함
            # y = 기존 y 보다 커야함
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            # x, y 의 위치는 dx, dy 값으로 인해 현재 위치 상하좌우 값임
            if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
                board[x][y] = 1
                dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                Q.append((x, y))

    if dis[6][6] == 0:  #
        print(-1)
    else:
        print(dis[6][6])

    return answer


print("답 : ", solution(8, 12))  # 80
