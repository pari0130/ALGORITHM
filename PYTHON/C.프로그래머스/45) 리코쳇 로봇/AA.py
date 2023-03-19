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

# 현재 위치의 상하좌우 좌표 값 위치 구하기 위한 변수
dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]


def DFS(x, y):
    # 2. 상하좌우 D 로 막혀있고 현재 좌표 G 면 Cnt += 1
    # 3. else
    # 4. 4 방향 range
    # 5. if 좌표 0,0 x,y 안에 있고 좌표에 지나간 자리가 아닌 경우에만
    global mx, my, R, new_board, answer, answer_list

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= mx and 0 <= yy <= my:
            while True:
                # D 를 만날때 까지 while
                prexx = xx - dx[i]
                preyy = yy - dy[i]
                nextxx = xx + dx[i]
                nextyy = yy + dy[i]

                if new_board[xx][yy] == "D":
                    answer += 1
                    if 0 <= prexx <= mx and 0 <= preyy <= my and new_board[prexx][preyy] == "G":
                        print()
                        print("GGGGG -> " + new_board[prexx][preyy])
                        answer_list.append(answer)
                        answer = 0
                        DFS(prexx, preyy)  # G 이전 "." 에서 다시 이동
                        new_board[prexx][preyy] = "."  # 이동 처리 후 돌아간 거리는 . 으로 초기화
                    break
                else:
                    if 0 <= nextxx <= mx and 0 <= nextyy <= my and \
                            (new_board[xx][yy] == "G" or new_board[xx][yy] == "."):
                        if new_board[xx][yy] == ".":
                            new_board[xx][yy] = "X"

                    xx = nextxx
                    yy = nextyy
                    # DFS(xx, yy)
                    # new_board[xx][yy] = "."  # 이동 처리 후 돌아간 거리는 . 으로 초기화


def solution(board):
    # 0. 좌표 사이즈 구해야 함, 0,0 ~ x,y
    # 1. for loop 출발점 R 좌표 얻어야 함 = 1
    global mx, my, R, new_board, answer, answer_list

    mx = len(board) - 1  # x max
    my = len(board[0]) - 1  # y max
    R = (0, 0)  # tuple R index R[0], R[1]
    new_board = [[""] * len(board[0]) for _ in range(len(board))]
    answer = 0
    answer_list = []
    answer_list.append(answer)

    # 시작 좌표 값 및 str new_board list
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                R = (i, j)
                break
            new_board[i][j] = board[i][j]

    new_board[R[0]][R[1]] = "X"
    DFS(R[0], R[1])

    if answer == 0:
        answer = -1
        answer_list.append(answer)

    return min(answer_list)


print("답 : ", solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))  # 7
print("답 : ", solution([".D.R", "....", ".G..", "...D"]))  # -1


## =========================================================================
def DFS2(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1  # 이동한 거리는 1로 체크
                DFS2(xx, yy)
                board[xx][yy] = 0  # 이동 처리 후 돌아간 거리는 0으로 초기화


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS2(0, 0)
    print(cnt)
