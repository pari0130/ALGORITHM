
# 섹션 3. 탐색&시뮬레이션.pdf
# a list, b list를 만들고 a[p1] < a[p2] 를 비교해서 c list append 시키는 문제
# 시간복잡도를 생각해서 n번만 돌수 있도록 해야함

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/4) 두 리스트 합치기"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
# c = list(range(n+m))

p1 = p2 = 0

c = []

while p1 < n and p2 < m:  # p1 혹은 p2가 n m 까지 갈 경우 까지
    if a[p1] <= b[p2]:  # p1와 p2를 비교해서 p2가 더 클 경우에는 c list에 먼저 p1을 append 함
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p2 < n:
    c = c + a[p1:]  # 배열의 길이가 다르므로 먼저 끝난 list의 남은 값을 c에 붙히는 방법임
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')
