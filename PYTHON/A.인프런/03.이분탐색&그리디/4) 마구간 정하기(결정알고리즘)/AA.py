
# 섹션 4. 이분탐색 and 그리디.pdf

'''
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/4) 마구간 정하기(결정알고리즘)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")


def Count(len):
    cnt = 1
    ep = Line[0]  # end point
    for i in range(1, n):
        if Line[i] - ep >= len:  # 마굿간 현재 index의 위치와 마굿간 end 위치 길이를 뺀 값이 전달받은 mid 보다 크면 답이 될 수 있는 조건
            cnt += 1
            ep = Line[i]  # 최초 end point는 0으로 해서 하나씩 증가 시키는 구조로 밀고 나가는 계산법
    return cnt


n, c = map(int, input().split())
Line = []
for _ in range(n):  # 입력받은 마굿간 길이를 list에 add
    tmp = int(input())
    Line.append(tmp)

Line.sort()
lt = 1
rt = Line[n - 1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2  # 이분탐색 절반값 구함
    if Count(mid) >= c:  # 마굿간 길이에 말이 몇마리 들어가는지 계산해서 들어가야되는 말의  길이 c보다 크거나 같으면 정답
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
