

'''


'''

import sys
from collections import deque
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/8) 사과나무(BFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 현재 위치의 상하좌우 좌표 값 위치 구하기 위한 변수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n // 2][n // 2] = 1  # 방문지점
sum += a[n // 2][n // 2]  # 출력 결과값
Q.append((n // 2, n // 2))
L = 0

while True:
    if L == n // 2:
        break
    size = len(Q)
    print("size : ", size)
    for i in range(size):  # 레벨탐색 구간 for
        tmp = Q.popleft()
        for j in range(4):  # 현재 가운데 좌표의 상하좌우 4방향 탐색
            # 큐에 입력된 ( 2, 2 ) 기준 tmp[0] => 2
            # 따라서 x = Q 0번위치, dx[-1] 위치 이므로 현재 위치 좌측 좌표를 구 할 수 있음
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:  # 좌표가 체크되어 있는지 체크 하는 부분
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))  # 괄호안에 괄호로 튜플 형태입력

    # print(L, size)
    # for x in ch:
    #     print(x)
    L += 1
print(sum)
