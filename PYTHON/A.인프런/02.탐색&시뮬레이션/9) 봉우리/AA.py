
# 섹션 3. 탐색&시뮬레이션.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/9) 봉우리"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# dx dy 0, 1, 2, 3 을 각각 읽으면 -1행 0열 a[i-1][j+0], 0행 1열a[i+0][j+1], 1행 0열a[i+1][j+0], 0행 -1열a[i+0][j-1]
# 앞으로 변수의 4방향 탐색을 이렇게 초기화 하도록 함
dx = [-1, 0, 1, 0]  # x a[x, y]
dy = [0, 1, 0, -1]  # y a[x, y]

# 배열 전체에 상하좌우 0 추가
n = int(input())  # 배열길이
a = [list(map(int, input().split())) for _ in range(n)]  # n*n 배열
a.insert(0, [0]*n)  # 0번행에 0으로 채워진 1차원 리스트 추가 .insert()
a.append([0] * n)  # 마지막행에 0으로 채워진 1차원 리스트 추가
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n + 1):  # for문은 1부터 n+1보다 작을떄 까지 돔
    # print('i : ', i)
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(len(dx))):  # 조건이 모두 참일때 참
            cnt += 1

print(cnt)
