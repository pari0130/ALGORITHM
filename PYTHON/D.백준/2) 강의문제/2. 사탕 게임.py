'''
https://www.acmicpc.net/problem/3085
'''
from itertools import *

n = int(input())  # 행
candy = [list(''.join(input())) for _ in range(n)]  # 배열
m = len(candy[0])  # 열
max = 0

def count():
    return 0


def search(i, j):
    print(candy[i][j])
    global n, m, max

    answer = 0

    for _ in range(4):
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            '''
            4방향 swap 후 swap 라인의 캔디 카운트
            카운트 대상은 스왑한 문자열 대상
            '''
            if count() > max:
                answer = max


for i in range(n):
    for j in range(m):
        search(i, j)

print(max)

#
# for i in range(n):
#     for j in range(m):
#         '''
#         현재위치 상하좌우 스왑, 스왑 후 인접 행, 열 count() > max check
#         '''
#         for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#             dy =
#             print()
#
#         s = swap()
#         if count() > max:
#             answer = max
#
#         print()

print(candy)

# 시간초과 함.....
