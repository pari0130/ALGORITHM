
# 섹션 3. 탐색&시뮬레이션.pdf

'''
# case 1 : 알고리즘 스럽게 짜려면 이와 같이
for i in range(n):
    s = input()
    s = s.upper()  # 대문자와 시킴
    size = len(s)  # 문자열 길이

    # print(s[-1])  # 파이썬에서는 마지막 배열을 -1로 접근 가능함
    for j in range(size // 2):
        if s[j] != s[-1 - j]:  # -1이 마지막 배열, -j 하는 이유는 마지막 배열에서 첫번쨰 배열의 길이만큼 추가로 빼주면서 길이 검증
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/11) 격자판 회문 수"
file = "/input.txt"
sys.stdin = open(path + file, "r")

board = [list(map(int, input().split())) for _ in range(7)]  # 7*7 격자판

cnt = 0

# case 01
for i in range(3):  # 0~5, 1~6, 2~7 총 7길이의 숫자 list를 5개 숫자씩 연속된것을 구하려면 3번 돌아야 함
    for j in range(7):  # 총 길이 7
        tmp = board[j][i:i + 5]  # [check] 행 고정 열 증가로 값 확인
        if tmp == tmp[::-1]:  # tmp 값이 tmp 역순 list 값과 같으면 cnt += 1
            cnt += 1
        for k in range(2):
            # [check] 행을 증가 열 고정, board[행+5(구하는길이)-(5/2니까 k는 2번)-1]
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1
print("답1 : ", cnt)

cnt = 0
# case 02
for i in range(3):  # 0~5, 1~6, 2~7 총 7길이의 숫자 list를 5개 숫자씩 연속된것을 구하려면 3번 돌아야 함
    for j in range(7):  # 총 길이 7
        tmp = board[j][i:i + 5]
        # 단순하게 5개의 배열 길이로 정해저 있을 경우 배열 0과 끝 -1 and 배열1과 끝-2 길이 비교
        if tmp[0] == tmp[-1] and tmp[1] == tmp[-2]:
            cnt += 1
        for k in range(2):
            # [check] 행을 증가 열 고정, board[행+5(구하는길이)-(5/2니까 k는 2번)-1]
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print("답2 : ", cnt)
