
# 섹션 4. 이분탐색 and 그리디.pdf

'''
증가수열을 만드는것임
lt 와 rt를 비교해서 작은값을 넣고 lt 혹은 rt위치를 이동시킴
lt 와 rt를 비교해서 작은값을 넣을때 그 숫자와 위치를 튜플 형식으로 넣음 (2, L)
다 넣은 후 튜플 list의 길이 출력, 문자열 출력 끝
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/9) 증가 수열 만들기(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())  # list 길이
a = list(map(int, input().split()))  # list
lt = 0
rt = n - 1
last = 0
res = ""
tmp = []
tmp2 = []
while lt <= rt:  # 증가수열 크기 비교
    print('last : ', last)
    print('a[lt] : ', a[lt])
    print('a[rt] : ', a[rt])

    if a[lt] > last:  # list와 비교하여 마지막에 저장된 자료보다 커야 증가수열에 저장되는 위치 임
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    print('tmp : ', tmp)
    if len(tmp) == 0:  # tmp에 아무런 값도 없는 경우 종료
        break
    else:
        res = res + tmp[0][1]  # 결과값 문자열 list에 [0][1] L, R 이 들어있는 문자 저장
        # [0][0] 의 의미는 tmp 0번index의 0번자료, 즉 a[lt] 혹은 a[rt] 숫자값이 last에 저장됨
        last = tmp[0][0]
        if tmp[0][1] == 'L':  # tmp의 1번자료 문자 확인
            lt += 1  # L인지 R인지 비교해서 lt혹은 rt값 위치 이동
        else:
            rt -= 1
    tmp2.append(tmp[0][0])
    tmp.clear()

print('list에 최종적으로 담긴 값 확인용 : ', tmp2)
print(len(res))
print(res)
