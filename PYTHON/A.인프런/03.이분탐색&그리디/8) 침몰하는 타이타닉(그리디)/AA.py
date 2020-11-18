
# 섹션 4. 이분탐색 and 그리디.pdf

'''


'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/8) 침몰하는 타이타닉(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0

while p:  # p list 가 존재할떄 까지
    if len(p) == 1:  # p list가 마지막에는 하나만 남게 될 수 있으므로 cnt만 증가 시키고 종료
        cnt += 1
        break

    if p[0] + p[-1] > limit:  # 0번과 n-1번을 합한 값이 리밋을 넘으면 정렬되어 있는 제일 큰 마지막 값만 pop
        p.pop()
        cnt += 1
    else:  # 그렇지 않을 경우 0번과 n-1번을 pop
        p.pop(0)
        p.pop()
        cnt += 1

print(cnt)
