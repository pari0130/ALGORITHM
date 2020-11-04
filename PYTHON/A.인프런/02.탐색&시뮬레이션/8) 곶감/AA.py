
# 섹션 3. 탐색&시뮬레이션.pdf


import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/8) 곶감"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())  # 배열길이
a = [list(map(int, input().split())) for _ in range(n)]  # n*n 배열
m = int(input())  # 변경시킬 숫자 배열길이

for i in range(m):  # 변경시킬 숫자 배열길이
    # 첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전하는 격자의 수입니다.
    # 변경시킬 숫자 배열
    h, t, k = map(int, input().split())
    if t == 0:  # 왼쪽방향
        for _ in range(k):
            # list에서 첫번째 index가 빠짐. 0번 index의 값. 그리고 뒤의 자료는 앞으로 당겨짐
            a[h - 1].append(a[h - 1].pop(0))
    else:  # 오른쪽 방향
        for _ in range(k):
            # list에서 첫번째 index가 빠짐. 0번 index의 값. 그리고 뒤의 자료는 앞으로 당겨짐
            a[h - 1].insert(0, a[h - 1].pop())  # pop만 하면 맨뒤의 자료를 가져옴

res = 0
s = 0 # 시작값 초기화
e = n - 1  # 5*5 라면 4번 마지막 열 / 시작값 초기화
# s = e = n//2 2로 나눈 몫은 2.. n이 5일때 배열의 수는 0~4이므로 가운데는 2가 됨..s
# 문제 포인트는 항상 홀수 라는 점 n = 항상 홀수

for i in range(n):
    for j in range(s, e + 1):  # j값은 0~1까지
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
