
# 섹션 4. 이분탐색 and 그리디.pdf

'''
팝을 쓸 경우 list가 있을때 pop후 0 1 2 3 4 5 중 0번이 제거되고 1번이 0번자리로 이동되는 비 효율적인 구조가 생길 수 있음
데큐를 사용해서 popleft를 쓰면 0번제거 후 1번으로 이동되서 1번 값이 제거됨
'''

import sys
from collections import deque
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/8) 침몰하는 타이타닉(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)  # 데큐 자료구조 선언
cnt = 0

while p:  # p list 가 존재할떄 까지
    if len(p) == 1:  # p list가 마지막에는 하나만 남게 될 수 있으므로 cnt만 증가 시키고 종료
        cnt += 1
        break

    if p[0] + p[-1] > limit:  # 0번과 n-1번을 합한 값이 리밋을 넘으면 정렬되어 있는 제일 큰 마지막 값만 pop
        p.pop()
        cnt += 1
    else:  # 그렇지 않을 경우 0번과 n-1번을 pop
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)
