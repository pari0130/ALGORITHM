'''

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/12) 단지번호 붙히기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 현재 위치의 상하좌우 좌표 값 위치 구하기 위한 변수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    # for x in board:
    #     print(x)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)  # 단지별로 개수 cnt ( 3개의 단지가 들어감 )
    print(len(res))
    res.sort()
    for x in res:
        print(x)
