
# 섹션 4. 이분탐색 and 그리디.pdf

'''
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/9) 증가 수열 만들기(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
last = 0
res = ""
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:  # tmp에 아무런 값도 없는 경우 종료
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':  # tmp의 1번자료 문자 확인
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)
