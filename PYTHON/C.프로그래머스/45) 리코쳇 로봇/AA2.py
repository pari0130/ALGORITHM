'''
https://school.programmers.co.kr/learn/courses/30/lessons/169199

R 의 위치에서 G 의 위치로 가야함
D 를 만나서 더이상 갈 수 없거나 끝지점일때의 G 를 만나면 횟수 종료
지나온 지점은 X 문자열로 지나온 지점 표시 후 reset

갈 필요 없는 좌표
- 0,0 0,4 4,0 4,4
- 상하좌우 D
- D 앞 G
- 상하좌우 순서로 이동

if
1. 이동 후 이동좌표 -1 지점에 G 가 있으면 종료
2. 이동 후 좌표의 끝지점에 G 가 있으면 종료

else


'''
from collections import deque

# 현재 위치의 상하좌우 좌표 값 위치 구하기 위한 변수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(board):
    cnt = 0
    answer_list = []
    board_q = deque()
    v = [[0] * len(board[0]) for _ in range(len(board))]

    # 시작 좌표 값 및 str new_board list
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                board_q.append((i, j, 0))
                v[i][j] = 1
                break

    while board_q:

        x, y, cnt = board_q.popleft()

        if board[x][y] == "G":
            return cnt

        for i in range(4):
            nextx = x
            nexty = y

            while 0 <= nextx + dx[i] < len(board) and 0 <= nexty + dy[i] < len(board[0]) and board[nextx + dx[i]][nexty + dy[i]] != "D":
                nextx += dx[i]
                nexty += dy[i]

            if not v[nextx][nexty]:
                board_q.append((nextx, nexty, cnt + 1))
                v[nextx][nexty] = 1

    return -1


print("답 : ", solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))  # 7
print("답 : ", solution([".D.R", "....", ".G..", "...D"]))  # -1


def solution2(board):
    que = []
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if board[x][y] == 'R':
                que.append((x, y, 0))
    visited = set()
    while que:
        x, y, length = que.pop(0)
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return length
        visited.add((x, y))
        for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + diff_x, now_y + diff_y
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
                    now_x, now_y = next_x, next_y
                    continue
                que.append((now_x, now_y, length + 1))
                break
    return -1


print("답 : ", solution2(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))  # 7
print("답 : ", solution2([".D.R", "....", ".G..", "...D"]))  # -1
