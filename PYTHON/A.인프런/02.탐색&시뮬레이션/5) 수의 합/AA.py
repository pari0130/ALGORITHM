
# 섹션 3. 탐색&시뮬레이션.pdf

# 입력받은 8(n) 배열을 순서대로 더해서 입력한 3(m) 과 같은 개수를 구함

# n = 8, a=0, m = 3, tot = 0, cnt = 0, lt = 0 (왼쪽 시작 지점), rt = lt+1(오른쪽 종료 지점)
# 입력받은 n list의 숫자를 받아서 a list 증가하며 lt + rt[rt-1] 개를 더함
# 1. tot가 m보다 작으면 rt를 증가 시켜서 lt + rt
# 2. tot가 m과 같으면 그만 더하고 lt를 증가시켜서 다시 lt+rt 반복 함
# 3. 봐야하는 if문은 tot < m, tot = m, tot > m 3개 임
# 4. cnt가 +=1 이 되면 tot는  0으로 초기화 해서 다시 3이 되는지 확인 해야함
# 4-1. 인강 해설에서는 tot를 초기화 하는게 아니라 tot 배열의 위치를 -1 함

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/5) 수의 합"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:  # 구하려는 합 m과 tot 크기 비교
        if rt < n:  # n (배열의 크기)가 rt의 위치 보다 작은지 비교함
            tot += a[rt]  # tot(합)에 a[rt] 위치 값을 더해줌
            rt += 1  # tot(합)이 구하려는 m 보다 작고 배열의 위치 n로 rt 보다 크니 rt위치 이동 시킴
        else:  # rt의 위치가 n보다 커지면 while 문 종료 시킴
            break
    elif tot == m:  # tot(합)이 구하려는 m과 같으므로
        cnt += 1  # 카운트 cnt 증가
        tot -= a[lt]  # 구하려는 3를 찾았으니 왼쪽 배열의 위치 이동
    else:
        tot -= a[lt]  # tot(합)이 구하려는 m 보다 클때는 항상 왼족 배열 위치 이동
        lt += 1

print(cnt)
