'''

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/14) 안전영역(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# sys.setrecursionlimit(1**6)  # 10의 6제곱의 재귀함수 타임 리밋


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):  # 4 방향 탐색
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == '__main__':
    n = int(input())  # 격자의 크기 n * n
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):  # 100 보다 작은 수를 찾으므로 100까지 돌면서 h 높이를 구함
        ch = [[0] * n for _ in range(n)]  # 0으로 초기화 된 2차원 list 초기
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)
