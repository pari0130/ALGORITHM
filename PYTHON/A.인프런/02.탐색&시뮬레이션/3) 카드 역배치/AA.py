
# 섹션 3. 탐색&시뮬레이션.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/3) 카드 역배치"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

# a, b = map(int, input().split())
# print(a, b)
# a, b = b, a  # 스와프
# print(a, b)
# as:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# list를 생성하게 되면 0번 인덱스 부터 생성되므로 21까지 해야 20

a = list(range(21))

print('as : ', a)
for _ in range(10):  # _ 언더바는 변수가 없을 것. 반복문만 도는것.
    s, e = map(int, input().split())
    # 2~7 구간일 경우 바꿔줘야할 인덱스는 2-7, 3-6, 4-5  / 3바퀴 돌려야힘
    # 7-2 // 2 할 경우 몫이 2가 되므로 2바퀴임. 그래서 +1을 해줘야 3바퀴가 맞음
    for i in range((e - s + 1) // 2):
        print('i : ', i)
        print('a : ', a[s + 1])
        print('b : ', a[e - i])
        # s+1의 이유는 list가 0번 index를 부터 이므로
        # i는 0부터 니까.. a[e-i] 해도 원하는 10을 찾음
        a[s + 1], a[e - i] = a[e - i], a[s + i]

a.pop(0)  # 0번 index 제거

for x in a:
    print(x, end=' ')
