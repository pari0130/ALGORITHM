'''

정수 1은 익은 토마토, 
정수 0은 익지 않은 토마토, 
정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

'''

import sys
from collections import deque
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/15) 토마토(BFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())  # 6열 4행 n 열, m 행
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
dis = [[0] * n for _ in range(m)]  # 익은 토마토 위치 저장 dis

for i in range(m):  # 행
    for j in range(n):  # 열
        if board[i][j] == 1:  # 익은 토마트 위치 라면
            Q.append((i, j))  # 위치의 값을 큐에 담는다

while Q:
    tmp = Q.popleft()
    for i in range(4):  # 4방향만 탐색
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1  # 익지않은 토마토를 1로 바꿔주고
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1  # dis에 일자 업데이트
            Q.append((xx, yy))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]

    print(result)
else:
    print(-1)
