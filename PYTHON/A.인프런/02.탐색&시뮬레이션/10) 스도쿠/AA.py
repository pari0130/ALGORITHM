
# 섹션 3. 탐색&시뮬레이션.pdf

'''
# 코드작성 팁
ch 0으로 초기화 한 9개 길이 list 
행체크, 열체크, 그룹체크 에 대한 각각 list
각 행 열 그룹을 돌면서 ch list에 1~9 숫자가 있으면 1을 채워서 합의 값이 9가 되면 true
asdasdasdasdasdasdasdsad
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/10) 스도쿠"
file = "/input.txt"
sys.stdin = open(path + file, "r")

a = [list(map(int, input().split())) for _ in range(9)]
# print(a)
# print(a[0][0])


def check(a):
    for i in range(9):  # 9개 list 행
        ch1 = [0] * 10  # list 초기화 10개
        ch2 = [0] * 10
        # print('check1 ch1 : ', ch1)
        # print('check1 i : ', i)

        for j in range(9):
            # print('check1 i : ', i, ' j : ', j)
            # print(a[i][j])
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
            print(ch1[j])

        print('check2 ch1 : ', ch1)
        # print('check2 ch2 : ', ch2)

        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    # i와 j는 그룹의 위치를 나타냄, 9x9일때 각 그룹은 3*3 이 되므로 [i][j] 값이 증가함에 따라 각 그룹이 loop
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10  # 이 위치에서 초기화 해주는 이유는 i와 j의 그룹 행열 for문 시작 점 이기 때문
            for k in range(3):
                for s in range(3):
                    # ch3 list는 a[그룹위치행 * 3 + 행][그룹위치열 * 3 + 열]
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:  # 각 그룹의 값이 9가 아닌 경우 return false
                return False
    return True


if check(a):
    print("yes")
else:
    print("no")
