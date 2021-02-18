'''

'''

import sys
from collections import deque
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/13) 섬나라 아일랜드(BFS 활용)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 시계방향 탐색, [-1,0] , [-1,1] ... 12시, 1시, 3시, 5시, 6시 ..  처리
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0  # 최초 1이 발견된 지점 0으로 초기화 하여 다시 방문하지 않도록 함
            Q.append((i, j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt += 1

print(cnt)
